# Licences and terms of use

Record of the terms governing every data source in this project, with verbatim text. Closes backlog tasks **F0.1**, **F0.2** and **F0.5**.

This document is the project's source of truth on licensing. If anything here contradicts the plan or the backlog, **this document wins**, because it is the only one that quotes the primary sources.

| Task | Status |
|---|---|
| F0.1 — Verbatim H&M clause | ✅ **Closed** — verbatim text in section 1 |
| F0.2 — Fashionpedia terms | ✅ **Closed** — verified on the official licence page |
| F0.5 — Decision on publishing weights | ✅ **Closed** — not published, see section 3 |

---

## 1. H&M Personalized Fashion Recommendations (Kaggle)

- **Competition sponsor:** H&M Hennes & Mauritz GBC AB, Mäster Samuelsgatan 46A, 106 38 Stockholm, Sweden
- **Competition website:** https://www.kaggle.com/c/h-and-m-personalized-fashion-recommendations
- **Official rules:** https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations/rules
- **Date consulted:** 14 September 2026
- **Role in the project:** primary source — catalog images, commercial metadata and transactions.

From the competition-specific terms header:

> **WINNER LICENSE TYPE:** Non-Exclusive
>
> **DATA ACCESS AND USE:** Non-Commercial Purposes & Academic Research

### 1.1 Verbatim text — Section 7, Competition Data

> **7. COMPETITION DATA.**
>
> "Competition Data" means the data or datasets available from the Competition Website for the purpose of use in the Competition, including any prototype or executable code provided on the Competition Website. The Competition Data will contain private and public test sets. Which data belongs to which set will not be made available to participants.
>
> **A. Data Access and Use.**
>
> Competition Use and Non-Commercial & Academic Research: You may access and use the Competition Data for non-commercial purposes only, including for participating in the Competition and on Kaggle.com forums, and for academic research and education. The Competition Sponsor reserves the right to disqualify any participant who uses the Competition Data other than as permitted by the Competition Website and these Rules.
>
> **B. Data Security.** You agree to use reasonable and suitable measures to prevent persons who have not formally agreed to these Rules from gaining access to the Competition Data. You agree not to transmit, duplicate, publish, redistribute or otherwise provide or make available the Competition Data to any party not participating in the Competition. You agree to notify Kaggle immediately upon learning of any possible unauthorized transmission of or unauthorized access to the Competition Data and agree to work with Kaggle to rectify any unauthorized transmission or access.
>
> **C. External Data.** You may use data other than the Competition Data ("External Data") to develop and test your Submissions. However, you will ensure the External Data is publicly available and equally accessible to use by all participants of the Competition for purposes of the competition at no cost to the other participants. The ability to use External Data under this Section 7.C (External Data) does not limit your other obligations under these Competition Rules, including but not limited to Section 11 (Winners Obligations).

### 1.2 Verbatim text — Section 8, Submission Code Requirements

> **8. SUBMISSION CODE REQUIREMENTS.**
>
> **A. Private Code Sharing.** Unless otherwise specifically permitted under the Competition Website or Competition Specific Rules above, during the Competition Period, you are not allowed to privately share source or executable code developed in connection with or based upon the Competition Data or other source or executable code relevant to the Competition ("Competition Code"). This prohibition includes sharing Competition Code between separate Teams, unless a Team merger occurs. Any such sharing of Competition Code is a breach of these Competition Rules and may result in disqualification.
>
> **B. Public Code Sharing.** You are permitted to publicly share Competition Code, provided that such public sharing does not violate the intellectual property rights of any third party. If you do choose to share Competition Code or other such code, you are required to share it on Kaggle.com on the discussion forum or notebooks/kernels associated specifically with the Competition for the benefit of all competitors. By so sharing, you are deemed to have licensed the shared code under a permissive (non-copyleft) Open Source Initiative-approved license (see www.opensource.org) that in no event limits commercial use of such Competition Code or model containing or depending on such Competition Code.
>
> **C. Use of Open Source.** Unless otherwise stated in the Specific Competition Rules above, if open source code is used in the model to generate the Submission, then you must only use open source code licensed under a permissive (non-copyleft) Open Source Initiative-approved license (see www.opensource.org) that in no event limits commercial use of such code or model containing or depending on such code.

### 1.3 Contrast with the earlier working formulation

The formulation the project had been using — *non-commercial, academic and educational use; transmission, publication or redistribution of the data to anyone who has not accepted the rules prohibited* — **is confirmed by the verbatim text**, and on one point is stricter than we assumed: 7.B prohibits making the data available to *"any party not participating in the Competition"*, not merely to those who have not accepted the rules.

**Nothing needs correcting** in sections 6.2, 7.3, 7.4 or 14 of the plan on the data side. What does need **adding** is section 1.4, which the plan did not contemplate.

### 1.4 Two new findings: section 8 was not in the plan

The plan analysed the restriction on **data**. The rules also restrict **code** and **dependency licensing**, and that affects concrete project decisions.

#### Finding 1 — Obligation to share code on Kaggle (8.B)

Read literally, 8.B says that if *Competition Code* is publicly shared, there is an obligation to share it **also on the competition's forum or notebooks on Kaggle**, and that doing so licenses it under a permissive OSI-approved licence.

The reading is not unambiguous:

- **For it applying:** 8.B carries no time limit, unlike 8.A, which explicitly says *"during the Competition Period"*. That drafting difference between two adjacent subsections is unlikely to be accidental.
- **Against it applying today:** the stated purpose is *"for the benefit of all competitors"*, which presupposes an active competition. The H&M competition closed in 2022.

**Decision: comply with the strict reading**, because it costs almost nothing and removes the ambiguity:

1. **Add a `LICENSE` file** with a permissive, non-copyleft OSI-approved licence — **MIT** (adopted). 8.B already implies this when it says *"you are deemed to have licensed"*; making it explicit beats leaving it inferred.
2. **Post a link to the repository** on the competition discussion forum, or a Kaggle notebook pointing to it.

Neither has any real cost and both are good practice regardless.

#### Finding 2 — Only permissive OSI dependencies (8.C)

8.C restricts open source used in the model to **permissive, non-copyleft, OSI-approved licences that do not limit commercial use**. Practical consequences:

- **Excluded:** copyleft licences (GPL, AGPL, LGPL in some uses) and anything with a non-commercial clause.
- **The planned stack complies:** PyTorch (BSD-3), scikit-learn (BSD-3), `transformers` (Apache-2.0), LightGBM (MIT), `implicit` (MIT), DuckDB (MIT), FAISS (MIT), OpenVINO (Apache-2.0).
- **The real risk is in model weights, not libraries.** Several vision-language models ship under non-commercial or bespoke licences that are not OSI-approved. This makes licence verification a **model selection criterion in F4**, alongside performance and cost — not a later formality.

---

## 2. Fashionpedia

- **Source:** https://fashionpedia.github.io/home/index.html
- **Licence and terms:** https://fashionpedia.github.io/home/data_license.html
- **Download repository:** https://github.com/cvdfoundation/fashionpedia
- **Date consulted:** 11 September 2026
- **Role in the project:** auxiliary source — visual intelligence and expert taxonomy.

### 2.1 Licence by component

Fashionpedia does not have a single licence. It has three, over three different components, with different obligations.

| Component | Licence | What it permits | What it requires |
|---|---|---|---|
| **Annotations and ontology** | Creative Commons Attribution 4.0 (CC BY 4.0) | Use, adaptation and redistribution, including commercial | Attribution to the Fashionpedia project in any use or derivative |
| **Images** | None of its own | Nothing on its own | The project **declares it does not own the copyright of the images**. Use must comply with each original source's terms, and the user accepts full responsibility for use of the dataset, including any copies of copyrighted images they create |
| **Dataset software** | BSD 2-Clause | Redistribution in source and binary form, including commercial use | Retain the copyright notice and conditions; no warranty |

### 2.2 Image sources

Images come from Flickr, Unsplash, Burst by Shopify, Freestocks, Kaboompics and Pexels. Each has its own terms.

**Consequence:** a public demo using Fashionpedia images requires **per-asset review**; accepting the annotations licence is not enough. This is why the F10.3 demo uses an own catalog and serves no Fashionpedia image files.

### 2.3 Compatibility with H&M clause 7.C

Fashionpedia is publicly available at no cost, satisfying the *External Data* requirement of section 7.C: *"publicly available and equally accessible to use by all participants… at no cost"*. Recorded for completeness, even though the competition is closed.

### 2.4 Required attribution

The CC BY 4.0 licence on the annotations requires attribution. Text to include in the README, the technical report and any derivative of the taxonomy:

> The taxonomy and attribute annotations used in this project come from the Fashionpedia project, licensed under Creative Commons Attribution 4.0.

And the citation the authors request:

```bibtex
@inproceedings{jia2020fashionpedia,
  title={Fashionpedia: Ontology, Segmentation, and an Attribute Localization Dataset},
  author={Jia, Menglin and Shi, Mengyun and Sirotenko, Mikhail and Cui, Yin and
          Cardie, Claire and Hariharan, Bharath and Adam, Hartwig and Belongie, Serge},
  booktitle={European Conference on Computer Vision (ECCV)},
  year={2020}
}
```

---

## 3. Decision: publishing weights fine-tuned on H&M

**Decision: they are not published.** Weights of any model fine-tuned on H&M data stay out of the public repository and out of any model registry reachable by third parties.

### 3.1 What the clause says — and does not say

Section 7.B enumerates prohibited acts on *"the Competition Data"*: transmit, duplicate, publish, redistribute or make available. **It does not mention derivative works or trained models.** Two readings are possible:

- **Restrictive:** weights are a derivative built on data whose redistribution is prohibited, and the clause's silence is not authorisation.
- **Permissive:** 7.B enumerates specific acts on *the data*, and trained weights are not the data.

### 3.2 Why the decision is not to publish, whichever reading prevails

There is a **technical** reason independent of the legal reading: model weights can memorise training examples, and in vision models that can allow partial reconstruction of images seen during training. Publishing weights is, to some degree, making available information derived from the restricted dataset.

And there is a **practical** one: in a portfolio project the value lies in the code, the report, the metrics and the demo. Weights fine-tuned on a dataset the reader cannot download are useless to anyone. Here the conservative decision is also the cheap one.

### 3.3 Status

**Closed and unconditional.** An earlier version of this document left the decision contingent on the verbatim text expressly authorising derivative works. The text has now been read and **says nothing about them**, so that condition is not met and will not be. It ceases to be an open item.

### 3.4 Scope

Covers weights of models fine-tuned or trained on H&M data. It does **not** cover third-party pre-trained models used unmodified, which are governed by their own licences — subject to the 8.C filter — and which are in no case redistributed from this repository.

---

## 4. Sources not incorporated

| Source | Terms | Status |
|---|---|---|
| **DeepFashion** (MMLab, CUHK) | Non-commercial research | Optional. If incorporated, the same no-data-publication rule applies. |
| **Amazon Reviews 2023** (McAuley Lab) | To be verified at the primary source | **Not used** until its terms are verified and recorded here. |

---

## 5. Reference literature

The academic papers underpinning the project **are read locally and not redistributed from the repository**. They live in `referencias/`, which is in `.gitignore`.

| Work | Where to consult it |
|---|---|
| Salminen, J., Yoganathan, V., Corporan, J., Jansen, B. J., & Jung, S.-G. (2019). *Machine learning approach to auto-tagging online content for content marketing efficiency*. Journal of Business Research, 101, 203–217. | Elsevier — https://doi.org/10.1016/j.jbusres.2019.04.018 |
| Sharma, V., & Karnick, H. (2016). *Automatic tagging and retrieval of E-Commerce products based on visual features*. Proceedings of NAACL-HLT 2016, 22–28. | ACL Anthology |

The *Journal of Business Research* article is an Elsevier publication under copyright: uploading the PDF to a public repository would be redistributing it. The NAACL paper has a more permissive licence, but it is still third-party literature and not a project artefact.

---

## 6. Derived actions

| Action | Origin | Status |
|---|---|---|
| Add `LICENSE` to the repository (MIT) | 8.B | ✅ Done |
| Post a link to the repository on the competition forum or a notebook | 8.B | ⬜ Pending (at publication, F10.6) |
| Verify a permissive OSI licence for every pre-trained model before adopting it | 8.C | ⬜ Selection criterion in F4 |
| Include CC BY 4.0 attribution to Fashionpedia in README and report | CC BY 4.0 | ✅ Done in README |

---

## 7. Verification log

| Date | What was verified | Outcome |
|---|---|---|
| 2026-09-11 | Fashionpedia terms on the official licence page | Three licences by component; third-party images. Section 2. |
| 2026-09-11 | H&M rules via programmatic access | **Failed.** The page renders client-side and requires a signed-in session. |
| 2026-09-14 | H&M rules, full text obtained with a signed-in session | Sections 7 and 8 transcribed verbatim. The earlier working formulation is confirmed; two new restrictions appear, covering code and dependencies (section 1.4). |

---

*This document is not legal advice. Its purpose is to record which terms govern the project, quoted from the primary source, so that decisions can be audited against the original documents rather than against a summary.*
