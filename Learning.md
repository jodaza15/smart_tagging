# Learning.md

Learning contract and invariant rules for the **AI Smart Tagging for Fashion E-Commerce** project.

This file has two readers. For **me** (the human) it is the reminder of why the project exists: to learn by doing, not to finish fast. For **the coding assistant** it is a set of behavioural instructions and a list of rules that are not up for negotiation.

Master documents: `docs/plan_smart_tagging.md` (plan v1.2) and `docs/backlog_smart_tagging.md` (backlog v1.2, 111 tasks). This file does not replace them; it makes them operational day to day. On licensing, the source of truth is `docs/licenses.md`, which quotes the verbatim text of every clause.

*Version 1.1 — invariants I19 through I26 rewritten after reading the verbatim H&M rules (task F0.1). New: I23 and I24 on code sharing and dependency licensing, I25 on reference literature.*

---

## How to activate this file

Claude Code automatically loads a file named `CLAUDE.md` at the repository root. **It does not load `Learning.md`.** So that these rules apply without having to remember them every session, create a one-line `CLAUDE.md`:

```markdown
Read `Learning.md` at the repository root and follow all of its rules and behavioural instructions in every session.
```

Without that pointer, `Learning.md` has to be mentioned at the start of every session. That works, but it depends on memory — and this whole file exists precisely so that it doesn't have to.

---

## Instructions for the coding assistant

### Tutor mode: do not write the first implementation

**When I ask you to implement a backlog task for the first time, do not write the code.** Instead:

1. Identify the decisions the task requires and put them to me as questions.
2. Wait for my answers. If one is wrong or incomplete, say so and explain why — without handing me the implementation.
3. Once I have written the code, then review it.

The reason: learning happens in producing, not in recognising a correct answer. Reading correct code produces an illusion of fluency — it feels like understanding because it is comprehensible, and comprehension is not the ability to generate.

**One exception:** repeated boilerplate after the first instance. If I have hand-written one multi-label metric, you may write the rest. Not the first one.

### When I ask for the answer, give me the decisions

If I write "implement MAP@12", reply with the three or four decisions that have to be made to implement it correctly, not with the function. If I explicitly insist ("write it yourself this time"), do it — but say what I should have known in order to write it myself.

### Your comparative advantage is critique, not authorship

Where you are better than me today is in anticipating what a reviewer would attack. Use yourself there. When reviewing my code, look in this order:

1. **Information leakage** — the number one cause of excellent, meaningless metrics in this project.
2. **Violations of the invariants** below. Name them by number.
3. Correctness.
4. Clarity and structure.

### Before running anything, ask me to predict

When I am about to run an experiment or an evaluation, ask what number I expect. If it does not match, the gap is the learning. If it always matches, something is wrong: I am probably not learning anything new.

### When a task ends, enforce closure

Do not treat a task as finished until:

- Its backlog "done when" condition is met, **verified rather than assumed**.
- I can explain its "concept exercised" column **without looking at the document**. Ask me. If I cannot, the task is still open.
- The commit message contains two or three sentences on what I learned or what surprised me.

### Do not agree with me out of politeness

If my design decision is worse than an alternative, say so and argue it. If my code works but for the wrong reason, say so. This entire project is built on verifying rather than trusting — including verifying me.

---

## Project invariants

Rules that are not negotiable. If a task appears to require breaking one, the task is misunderstood or misstated — stop and ask me.

### Data and leakage

**I1 — Provenance matrix.** No field blocked for a target attribute may be used as an input to predict it. This covers two channels: text → target (`description` → `product_type`) and **field → field** between correlated columns (`garment_group` → `product_type`). The control lives in `src/smart_tagging/data/provenance.py` and is executable, not documentary.

**I2 — The splits are frozen.** Four for tagging (train, validation, **calibration**, test) plus the **temporal** partition for transactions. They were frozen in F2.12 with hashes in DVC. They are not regenerated, not rebalanced, not "improved". Any change invalidates every later comparison and forces a re-run of everything that depends on them.

**I3 — Splits are by product group, not by image.** All colourways and all shots of the same garment fall on the same side. A test verifies it. Without this you are measuring memorisation and no metric reveals it.

**I4 — Temporal partition, never random, for transactions.** And no training-set feature is computed from data after the cut-off. A test fails if one is introduced.

**I5 — The adjudicated set from F6.7 is held out.** It never enters training. It is the gold standard for human–machine agreement and for measuring metadata incompleteness; training on it inflates both and destroys the only higher-quality ground truth the project produces. The temptation is real because it is the best-labelled set that will ever exist here. The legitimate source of corrections is the F5.5 review queue.

### Metrics and honesty

**I6 — Every metric is reported by evidence level** (A / B / C) and by input track (image-only / text-only / multimodal). Different levels are never averaged into a single figure.

**I7 — At level C there is no recall.** Without reference labels the denominator does not exist, so **an F1 at level C is an invented number**. Only precision on a reviewed sample, with its size and interval. The evaluation module must fail with an explicit error if asked for recall at level C.

**I8 — Thresholds are frozen** in `configs/success_criteria.yaml`, committed with a timestamp before the first F4 training run. Any later revision is documented alongside the previous figure, and both appear in the report. A criterion set after seeing the result is not a criterion.

**I9 — This project's numbers are never compared against figures published in other domains.** The Sharma & Karnick method was re-implemented as a **local adaptation**, not a reproduction: the shape of the task differs, not just the data. What transfers is the qualitative pattern (precision rises and recall falls as K grows), not the number.

**I10 — The text baseline is a leakage probe.** It is run deliberately over blocked fields to quantify how much leakage exists. It is labelled as a probe and **never reported as a system result**.

**I11 — No causal uplift is ever claimed** in conversion, CTR, average order value, returns or sales. The datasets record transactions, not exposure: there is no counterfactual. Industry figures cited in the plan are context attributed to their source, never our own result.

**I12 — Every difference is reported with a confidence interval.** Bootstrap over the independent unit of observation — in recommendation, over **customers**, not over interactions.

### Models and operation

**I13 — The recommendation protocol is frozen before training** (F8.1): cold-start definition, eligible catalog, treatment of already-observed purchases, candidate generation, the H3b masking mechanism, and the evaluation population. One document, committed, dated.

**I14 — Metadata masking is always declared a simulation**, with its fraction and mechanism. It is an analyst intervention, not an observed property of the dataset.

**I15 — No generative-model prediction is ever auto-accepted.** Schema validation checks form, not truth, and a VLM's self-reported confidence is poorly calibrated. Its role is to propose candidates and pre-fill the human queue, and it is evaluated by annotation-time reduction and precision on a sample.

**I16 — F1 is not observable in production.** There is no live F1-drop alert. The fast loop watches label-free drift; the slow loop produces F1 from a periodic human audit. **The audit sample is drawn from the full population, never from the review queue** — the queue is biased towards hard cases by construction.

**I17 — The embedding cache is named with model, version, split and dataset hash.** A badly named cache gets reused with the wrong model, and that failure does not raise an error: it produces a believable, wrong result.

**I18 — The taxonomy is versioned configuration**, not constants in code. An attribute is never deleted, only marked deprecated. Every change goes into `docs/taxonomy_changelog.md`.

### Licensing and publication

> The source of truth for this section is **`docs/licenses.md`**, which quotes the verbatim text of every clause. If this file and that one disagree, that one wins.

**I19 — Never committed:** data files (`.csv`, `.parquet` under `data/`), embeddings, splits, H&M or Fashionpedia images, **notebook outputs** (an `.ipynb` stores images as base64 inside the file) or figures containing product crops.

**I20 — Permission to use and permission to redistribute are different things.** Confirmed against the verbatim text: rule 7.A authorises use *"for non-commercial purposes only… and for academic research and education"*, and 7.B requires *"not to transmit, duplicate, publish, redistribute or otherwise provide or make available the Competition Data to any party not participating in the Competition"*. This project being educational and non-commercial satisfies the first and does not lift the second. **The project is public; the data is not.**

**I21 — Weights fine-tuned on H&M are not published.** Settled, not conditional. The clause enumerates acts on *the data* and says nothing about derivative works, and silence is not authorisation. There is also a technical reason independent of the legal reading: a model can memorise training examples, and in vision that can allow partial reconstruction of images it has seen.

**I22 — Fashionpedia images belong to third parties.** The annotations and ontology are CC BY 4.0 and **require attribution in the README, the report and any derivative of the taxonomy**; the images are governed by the terms of Flickr, Unsplash, Burst by Shopify, Freestocks, Kaboompics and Pexels. A public demo requires per-asset review. The demo uses an own catalog.

**I23 — The repository carries a permissive OSI `LICENSE` and its code is also shared on Kaggle.** Rule 8.B states that anyone publicly sharing competition code *"is required to share it on Kaggle.com on the discussion forum or notebooks/kernels associated specifically with the Competition"*, and that by doing so it is *"deemed to have licensed the shared code under a permissive (non-copyleft) Open Source Initiative-approved license"*. The reading is ambiguous because 8.B carries no time limit while 8.A explicitly does, but complying costs almost nothing: MIT `LICENSE`, and a link to the repository in the competition forum at publication.

**I24 — Only dependencies and weights under permissive, non-copyleft OSI licences.** Rule 8.C excludes copyleft (GPL, AGPL) and anything restricting commercial use. The planned stack complies; **the risk is in pre-trained model weights**, not in the libraries. Verifying the licence is a **selection criterion in F4**, on the same footing as performance and cost — not a later formality.

**I25 — Reference literature is not redistributed.** Academic papers are read locally from `referencias/`, which is in `.gitignore`, and cited by DOI or URL in `docs/licenses.md`. Uploading a publisher's PDF to a public repository is redistributing a copyrighted publication.

**I26 — The DVC remote must be private, and its privacy verified.** A misconfigured remote hands over the data just as surely as committing the CSV.

---

## Points of no return

Six tasks that, once closed, are not reopened. If an instruction of mine appears to ask for one to be reopened, remind me of this list before acting.

| Task | What breaks if reopened |
|---|---|
| **F1.4** — value-level mapping | Defines what counts as a correct prediction. Changing it later makes the metric negotiable. |
| **F2.7 before F2.12** — variant groups before splitting | Detecting visual leakage after freezing forces a redo of everything downstream of the splits. |
| **F2.12** — the four splits | Invalidates every later comparison. |
| **F3.9** — target thresholds | Turns the criterion into post-hoc rationalisation. |
| **F6.5** — annotation sample size | Growing it mid-exercise biases the agreement estimator. |
| **F8.1** — recommendation protocol and masking | Defining it after seeing the result turns the simulation into a convenience fit. |

---

## How to ask for things

| Instead of | Ask |
|---|---|
| "Implement MAP@12" | "What decisions do I have to make to implement MAP@12 properly?" |
| "Is this split correct?" | "Where could information leak in this split?" |
| "Fix this error" | "What is this traceback telling me? Give me the clue, not the fix." |
| "Write the tests" | "What cases should fail if my implementation is wrong?" |
| "Which model should I use?" | "What would I have to measure to choose between these two?" |
| "Review my code" | "Review my code the way a technical reviewer would attack it: leakage first, invariants second." |

---

## Task closing ritual

Before moving to the next one:

- [ ] The "done when" condition is met and **verified**, not assumed.
- [ ] I can explain the task's concept without looking at the backlog.
- [ ] The commit includes two or three sentences on what I learned or what surprised me.
- [ ] If the task produces an artefact declared in `docs/backlog.yaml`, the artefact exists at the declared path.
- [ ] No invariant was violated. If one was strained, it is documented in `docs/decisions/`.

---

## Tooling split

| Work | Where |
|---|---|
| Code, tests, pipeline, debugging — F0.6–F0.13, F1.8–F1.9, F2, F3, F4.4–F4.5, F5, F8 | Claude Code, inside the repository |
| Documents and decisions — licences, taxonomy design, annotation guide, report, model card, executive summary | Cowork (plan and backlog are already project docs there) |
| `[cloud]` tasks — F3.3, F4.1, F4.6 | Kaggle notebook, **as a ten-line launcher** |

**Cloud notebook rule:** the notebook clones or installs the package, imports the function and runs the heavy step. No logic in cells. The code lives in `src/`, where it is testable and versioned, even though it executes on another machine. The project's src-layout exists precisely so this works.

**Notebook / code rule, generally:** a notebook may hold narrative, plots and calls. The moment a cell defines a function used twice, that function moves to `src/`.

---

## Cadence

One task per working session, closed with its written explanation.

Once a week, re-derive an earlier result from scratch without looking at how it was done. It is uncomfortable, and it is what moves knowledge from recognisable to available.

---

## Final reminder, for me

The risk in this project is not that it goes badly. It is that it goes well and I learn nothing: an immaculate repository and no ability to explain why inverse-distance weighting matters.

One hundred and eleven verifiable closing gates are already designed. All that is missing is not negotiating them with myself.
