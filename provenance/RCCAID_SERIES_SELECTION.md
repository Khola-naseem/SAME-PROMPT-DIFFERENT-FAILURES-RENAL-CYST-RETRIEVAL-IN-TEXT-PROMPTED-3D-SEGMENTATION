# RCC-AID series selection

RCC-AID v2.0.0 contains 129 annotated CT series from 91 patients. The audit
uses exactly one frozen series per patient, so its independent experimental
unit is the patient and its RCC-AID denominator is 91 rather than 129.

## Frozen 60-patient audit

The first stage was frozen on 2026-09-27 before image download and inference.
It included all 30 patients with an annotated cyst-positive series. When a
patient had more than one cyst-positive series, one was selected by a fixed
salted SHA-256 rank without using cyst size. Thirty distinct patients with a
cyst-negative, tumor-positive series were then matched one to one to the
positive cases by collection and contrast phase using Hungarian assignment;
a salted hash resolved ties. Model outputs and downstream performance did not
enter selection.

- Salt: `CystPrompt3D-RCC-AID-external-2026-09-27-v1`
- Frozen manifest SHA-256:
  `05dea55dfedd8893f13a6e536d8b13f7ad9af65ba9a1cbf19a8d84d501eca84e`

## Remaining 31 patients

The second stage was frozen on 2026-10-06 and included every patient absent
from the 60-patient manifest exactly once. For a patient with an eligible
tumor-positive series, one such series was chosen by a second fixed salted
SHA-256 rank; otherwise one annotated series was chosen by the same rank.
Model output, intensity, lesion size, morphology, and downstream performance
were not used. Later correction of scaled-label integer conversion changed
the reported cyst/tumor status of some selected volumes but did not change any
selected patient or SeriesInstanceUID. Under the corrected labels, the full
91-patient cohort contains 32 cyst-positive and 59 cyst-negative volumes.

- Salt: `CystPrompt3D-RCCAID-fresh-negative-confirmation-2026-10-06-v1`
- Frozen manifest SHA-256:
  `612b80f8b270918a6ecbd6ab38eddfb3648fe4da47761016076970c6e46b5496`
- Source 129-series inventory SHA-256:
  `8b70378e7c045acc320fae4d410527eb4b355597c9693154afa564d12dc50869`

Every selected volume was subsequently joined to the official metadata by
exact SeriesInstanceUID. The 91 selected acquisitions comprise 17 arterial,
35 venous, and 39 delayed series. No patient contributes more than one series,
and phase-stratified analyses are therefore between-patient comparisons.

## Public selected-series manifest

`rccaid_selected_series.csv` lists the exact 91 selected SeriesInstanceUIDs,
public case IDs, selection stage, corrected reference group, collection,
contrast phase, and acquisition tag. It excludes local filesystem paths,
patient-level model outputs, and voxel counts. The corrected reference groups
contain 32 cyst-positive/tumor-positive and 59 cyst-negative/tumor-positive
volumes. The manifest is checked by `scripts/validate_release.py` for 91 unique
case IDs and SeriesInstanceUIDs, the 60/31 stage split, the 32/59 reference-
group split, and the 17/35/39 phase counts.
