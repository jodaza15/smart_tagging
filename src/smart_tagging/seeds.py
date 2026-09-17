"""Deterministic seeding for every random source this project touches.

Reproducibility is a claim, and a claim needs evidence. `set_seeds` therefore
reports what it actually seeded rather than assuming: a run whose record says
``torch=False`` had no deterministic GPU work, and that is something worth
having written down at the time instead of guessed at months later.

Known limitations, stated rather than hidden:

- ``PYTHONHASHSEED`` only takes effect before the interpreter starts. Setting it
  from inside a running process does nothing, so this module reports whether it
  was set rather than pretending to control it.
- Seeding makes torch's *sampling* reproducible, not its *kernels*. Bitwise
  determinism on GPU additionally needs ``torch.use_deterministic_algorithms``
  and cuDNN flags, which cost throughput and raise for ops without a
  deterministic implementation. That belongs with the first training run (F4),
  where the trade-off can be measured, not here.
"""

from __future__ import annotations

import os
import random
from dataclasses import asdict, dataclass

import numpy as np

__all__ = ["SeedReport", "set_seeds"]


@dataclass(frozen=True)
class SeedReport:
    """What a call to `set_seeds` actually managed to seed.

    Log this next to the run. "The run was seeded" is not verifiable after the
    fact; "python=True, numpy=True, torch=False" is.
    """

    seed: int
    python: bool
    numpy: bool
    torch: bool
    torch_cuda: bool
    pythonhashseed: str | None

    def as_tags(self) -> dict[str, str]:
        """Flatten to strings, ready to attach to an experiment run."""
        return {f"seed.{k}": str(v) for k, v in asdict(self).items()}


def set_seeds(seed: int) -> SeedReport:
    """Seed every generator available in this process and report the result.

    There is no default seed on purpose. The seed is part of what identifies a
    run, alongside the commit and the configuration, so it has to be chosen and
    recorded by the caller rather than inherited silently from this module.
    """
    random.seed(seed)

    # Seeds the legacy global RandomState, which is what scikit-learn and much
    # of the ecosystem still reach for when no generator is passed explicitly.
    # Project code should prefer an explicit np.random.default_rng(seed) handed
    # down through call arguments: global state is exactly the kind of hidden
    # coupling that makes a result impossible to reproduce in isolation.
    np.random.seed(seed)

    torch_seeded = False
    cuda_seeded = False
    try:
        import torch
    except ImportError:
        # Expected: torch is an optional extra, and CI installs the package
        # without it. Caught narrowly on purpose — a bare `except` here would
        # swallow a torch that is installed but broken, leaving an unseeded
        # generator behind a report that claims everything is fine.
        pass
    else:
        torch.manual_seed(seed)
        torch_seeded = True
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)
            cuda_seeded = True

    return SeedReport(
        seed=seed,
        python=True,
        numpy=True,
        torch=torch_seeded,
        torch_cuda=cuda_seeded,
        pythonhashseed=os.environ.get("PYTHONHASHSEED"),
    )
