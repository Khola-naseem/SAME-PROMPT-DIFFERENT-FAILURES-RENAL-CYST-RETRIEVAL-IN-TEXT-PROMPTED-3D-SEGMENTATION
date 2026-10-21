# Reproducibility scope

This repository is the public, aggregate reproducibility record for the study.
It separates two evaluation regimes that answer different questions.

## Label-free scale audit

The main released-checkpoint audit used 409 KiTS23 scans and all 91 RCC-AID
v2.0.0 patients. A full-volume SAT-Pro kidney query supplied the crop center;
no reference label, cyst status, or tumor status entered crop construction or
model inference. All five checkpoints received the same physical crop, and
their predictions were restored to the original CT grid before evaluation.

## Reference-assisted supporting analyses

Probability-based FROC, fixed-region discrimination, and spatial-utility
analyses used predefined 60-case subsets from each domain. Their crops came
from the reference renal bounding box with a 50-mm margin. These results test
behavior within a controlled renal search region and should not be described
as whole-volume retrieval.

## Cohort roles

The released checkpoints were evaluated without weight updates. The KiTS23
scale cohort includes 349 cases that were used to fit separate local nnU-Net
comparators; those local models were evaluated only on the disjoint 60-case
KiTS23 audit subset. Local-model results must not be extrapolated to all 409
KiTS23 scans. The RCC-AID scale audit includes all 91 patients.

## Prompt mapping

The canonical concepts were `kidney`, `kidney cyst`, and `kidney tumor`.
VoxTell, Medical-SAM3, and BiomedParse received independent literal concept
queries. SegVol received each concept through its released CT sentence
template. SAT-Pro received kidney and kidney cyst in a joint query context and
kidney tumor in a separate query, matching the evaluated native interface.

## Integrity

Run the following command after cloning:

```bash
python3 scripts/validate_release.py
```

The validator parses the frozen JSON files and aggregate CSV tables, checks
the five checkpoint digests recorded in the provenance table, rejects local
paths and common credential patterns, and verifies every released file against
`ARTIFACT_SHA256.txt`.
