# SAME-PROMPT-DIFFERENT-FAILURES: RENAL-CYST-RETRIEVAL-IN-TEXT-PROMPTED-3D-SEGMENTATION

Reproducibility records for the renal CT concept-retrieval audit of five
released text-promptable 3D segmentation checkpoints.


## What this release does not contain

This repository does not redistribute CT volumes, annotations, model weights,
patient-level predictions, probability maps, or local filesystem paths. Obtain
datasets and checkpoints from their original providers under their respective
terms. The hashes in `provenance/checkpoints.csv` identify the exact local
files evaluated by the study.

## Evaluation regimes

### Main label-free scale audit

- 409 KiTS23 scans and one frozen annotated CT series from each of all 91
  RCC-AID v2.0.0 patients. RCC-AID contains 129 annotated series in total;
  series-selection provenance is documented in
  `provenance/RCCAID_SERIES_SELECTION.md`, and the 91 selected
  SeriesInstanceUIDs are listed in `provenance/rccaid_selected_series.csv`.
- Canonical prompts: `kidney`, `kidney cyst`, and `kidney tumor`. The literal
  concepts were passed directly to VoxTell, Medical-SAM3, and BiomedParse,
  inserted into SegVol's released CT sentence template, and supplied to
  SAT-Pro with `kidney` and `kidney cyst` in one query context and the tumor
  concept separately.
- One label-free kidney-centered physical crop shared across checkpoints.
- Predictions restored to the original CT grids before endpoint evaluation.

### Supporting reference-assisted analyses

- Predefined 60-case subset per domain: 30 cyst-positive and 30
  cyst-negative cases.
- Reference renal bounding box with a 50-mm margin at native spacing.
- Used for probability-based FROC, fixed-region, and spatial-utility analyses.

Results from these regimes are labeled separately and should not be pooled.

## Repository layout

```text
configs/       frozen evaluation specifications
provenance/    checkpoint hashes, commits, and class-supervision evidence
results/       aggregate, non-patient-level analysis tables
figures/       manuscript figures derived from aggregate results
scripts/       release-integrity validation
```



## Upstream models and datasets

- [VoxTell](https://github.com/MIC-DKFZ/VoxTell)
- [SAT](https://github.com/zhaoziheng/SAT) and
  [SAT-DS](https://github.com/zhaoziheng/SAT-DS)
- [SegVol](https://github.com/BAAI-DCAI/SegVol)
- [Medical-SAM3](https://github.com/AIM-Research-Lab/Medical-SAM3)
- [BiomedParse v2](https://github.com/microsoft/BiomedParse/tree/v2)
- [KiTS23](https://kits-challenge.org/kits23/)
- [RCC-AID v2.0.0](https://doi.org/10.5281/zenodo.20719257)

## Citation and license

Please cite the associated manuscript; its formal citation will be added after
publication. No reuse license is granted by this repository at present.
Upstream data and checkpoint licenses remain with their respective providers.
