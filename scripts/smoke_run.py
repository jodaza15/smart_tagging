"""Record one throwaway MLflow run, to prove the tracking backend works (F0.7).

Not a test: it writes to the tracking store, which tests must never do. Run it once by
hand and look at the result in the MLflow UI:

    uv run python scripts/smoke_run.py
    uv run mlflow ui --backend-store-uri sqlite:///mlflow.db
"""

import mlflow

from smart_tagging.seeds import set_seeds
from smart_tagging.tracking import start_run

SEED = 20260917


def main() -> None:
    report = set_seeds(SEED)

    with start_run(
        hypothesis="H0-smoke",
        splits_version="none",
        run_name="backend-smoke-test",
        seed_tags=report.as_tags(),
    ):
        mlflow.log_param("fake_parameter", 42)
        mlflow.log_metric("fake_metric", 0.5)

    print(f"seeded: {report}")


if __name__ == "__main__":
    main()
