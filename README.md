# AI Smart Tagging for Fashion E-Commerce

An automated catalog tagging system: it takes a product image and returns **structured attributes over a controlled taxonomy** — garment category, colour, pattern, silhouette, apparent material — with a confidence score per attribute.

Built as a retail data science project on public datasets, with one goal that separates it from a classification exercise: measuring not just whether the model is right, but **whether the attributes it generates are worth anything to the business**.

---

## The questions this project asks

Three chained experiments, each with its metric and its acceptance criterion frozen *before* looking at the result:

| | Question | Metric |
|---|---|---|
| **1. Quality** | Can AI tag a catalog with accuracy comparable to a human annotator? | Per-attribute F1 by evidence level; human–machine agreement using a chance-corrected statistic |
| **2. Discovery** | Do generated attributes surface products better than traditional metadata? | NDCG@10 over blind human relevance judgements |
| **3. Value** | Does enriching a recommender with those attributes improve it, and under what conditions? | MAP@12, under complete metadata and under simulated incomplete metadata |

The third is what makes this more than a computer vision exercise. The finding to report is not *"I fine-tuned a model and got 91% accuracy"* but *"adding AI-generated visual attributes moved MAP@12 by X%, with the effect concentrated in the regime where catalog metadata is incomplete"* — which is the problem Smart Tagging actually solves in production.

## What this project does *not* demonstrate

Declared up front, because it is the project's structural limitation:

- **No causal uplift in conversion, CTR, average order value or sales.** The public datasets record transactions, not exposure: without impressions or clickstream there is no counterfactual.
- **No online A/B testing.** All evaluation is offline.
- **No F1 on attributes without ground truth.** With no reference labels, recall is not computable, so at that level only precision on a reviewed sample is reported.

Industry figures cited in the plan are market context attributed to their source, never results of this project.

## Status

**Phase F0 — framing and environment.** Planning is closed; execution is starting. There are no results yet.

| Phase | Status |
|---|---|
| F0 · Framing, licences and environment | 🔨 In progress |
| F1 · Taxonomy and ontology | ⬜ |
| F2 · Data, EDA and frozen splits | ⬜ |
| F3 · Baselines | ⬜ |
| F4 · Tagging model | ⬜ |
| F5 · Calibration and human-in-the-loop | ⬜ |
| F6 · Human evaluation | ⬜ |
| F8 · Business value | ⬜ |
| F7 · Semantic search *(extension)* | ⬜ |
| F9 · Product and MLOps *(extension)* | ⬜ |
| F10 · Close and publication | ⬜ |

The full breakdown is 111 tasks in [`docs/backlog_smart_tagging.md`](docs/backlog_smart_tagging.md).

---

## Data

The project uses two public sources and **neither is distributed from this repository**:

- **H&M Personalized Fashion Recommendations** (Kaggle) — primary source: catalog images, commercial metadata and transactions.
- **Fashionpedia** — auxiliary source: expert-built taxonomy and fine-grained annotated attributes.

Instructions for obtaining them are in [`data/README.md`](data/README.md). The test suite runs without downloading anything, using the synthetic fixtures in `tests/fixtures/`.

### Why the data is not in this repository

The H&M competition rules authorise non-commercial, academic and educational use, and at the same time require participants *"not to transmit, duplicate, publish, redistribute or otherwise provide or make available the Competition Data to any party not participating in the Competition"*.

**Permission to use and permission to redistribute are two different things, and the second does not follow from the first.** This project being educational and non-commercial satisfies the use condition; it does not lift the redistribution prohibition, because that clause does not turn on whether money changes hands but on who receives the data.

Hence the rule that governs this repository: **the project is public, the data is not.**

### Publication contract

| Published | Not published |
|---|---|
| Code, notebooks and the full pipeline | Images, CSVs and any data file |
| Technical report, aggregate metrics, tables and figures | Embeddings, derived features and computed splits |
| Taxonomy, attribute schema and mappings | Weights of models fine-tuned on H&M |
| Model card, error analysis and calibration curves | Any demo served with H&M data |
| Demo with an own catalog of redistributable images | Fashionpedia images without per-asset review |

The full detail, with the verbatim text of each clause, is in [`docs/licenses.md`](docs/licenses.md).

---

## Licences and attribution

The code in this repository is released under the [MIT License](LICENSE).

> The taxonomy and attribute annotations used in this project come from the **Fashionpedia** project, licensed under **Creative Commons Attribution 4.0**.

```bibtex
@inproceedings{jia2020fashionpedia,
  title={Fashionpedia: Ontology, Segmentation, and an Attribute Localization Dataset},
  author={Jia, Menglin and Shi, Mengyun and Sirotenko, Mikhail and Cui, Yin and
          Cardie, Claire and Hariharan, Bharath and Adam, Hartwig and Belongie, Serge},
  booktitle={European Conference on Computer Vision (ECCV)},
  year={2020}
}
```

Fashionpedia images are owned by third parties — Flickr, Unsplash, Burst by Shopify, Freestocks, Kaboompics and Pexels — and are not redistributed here.

The academic literature underpinning the project is cited by DOI in `docs/licenses.md` and is not redistributed.

---

## Repository layout

```
smart_tagging/
├── notebooks/          # narrative and exploration; they import from src/
├── src/smart_tagging/
│   ├── taxonomy/       # layer zero: versioned attribute schema
│   ├── data/           # ingestion, splits and leakage control
│   ├── features/       # embedding extraction and cache
│   ├── models/         # multi-label tagging
│   ├── calibration/    # confidence, thresholds and coverage
│   ├── recommender/    # business-value experiment
│   ├── evaluation/     # metrics per attribute and evidence level
│   └── serving/        # inference API
├── configs/            # taxonomy, mappings, success criteria
├── tests/fixtures/     # public synthetic data
├── docs/               # plan, backlog, licences, decisions
├── reports/            # generated figures and metrics
├── data/               # excluded from Git
└── artifacts/          # embedding cache, excluded from Git
```

## Documentation

| Document | Contents |
|---|---|
| [`Learning.md`](Learning.md) | Learning contract and the project's 26 invariants |
| [`docs/plan_smart_tagging.md`](docs/plan_smart_tagging.md) | Full plan: objectives, architecture, models, metrics, risks |
| [`docs/backlog_smart_tagging.md`](docs/backlog_smart_tagging.md) | 111 tasks, each with the concept it exercises |
| [`docs/licenses.md`](docs/licenses.md) | Terms of each source, with verbatim text |

---

## Design decisions worth a look

For anyone reviewing this repository with a technical eye, these are the decisions where the judgement lives:

- **Evidence levels A/B/C per attribute.** The taxonomy is richer than the catalog's verifiable attributes, so metrics are reported separately by the kind of ground truth available and are never averaged across levels. At level C recall is not computable, so no F1 is reported there — reporting one would be inventing half the number.
- **Executable provenance matrix.** Leakage control is code with tests, not a document: it covers the text→target channel and the field→field channel between correlated columns, which is the one that gets overlooked.
- **Splitting by product group, not by image.** In fashion catalogs the same garment appears in several colourways with near-identical photos; splitting by image measures memorisation and no metric reveals it.
- **Thresholds frozen before training.** Calibrated on the baseline and committed with a timestamp, so the criterion cannot be chosen after the result is known.
- **Label-free production monitoring.** In production F1 is not observable, so drift is watched with signals that need no ground truth and F1 comes from a periodic audited sample drawn from the population — never from the review queue, which is biased towards hard cases by construction.

---

## Author

**José David Zamudio** — [github.com/jodaza15](https://github.com/jodaza15)

*A Spanish-language version of the planning documents is kept in `docs/` for reference.*
