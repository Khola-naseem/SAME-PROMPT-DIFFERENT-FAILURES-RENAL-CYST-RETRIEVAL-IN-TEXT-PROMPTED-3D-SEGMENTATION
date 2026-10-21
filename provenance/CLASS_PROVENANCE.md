# Kidney-cyst supervision provenance

Every audited checkpoint has released evidence for a separately supervised
renal-cyst concept. This supports interpretation as retrieval of a supervised
concept. It does not establish that every audited patient was absent from the
checkpoint's original training data.

| Model | Separate cyst supervision | Training source represented | Evidence | Interpretation |
|---|---:|---|---|---|
| VoxTell v1.1 | Yes | KiTS23 | The official supplement lists KiTS23 kidney, kidney-tumor, and kidney-cyst targets; the v1.1 model card states that the paper datasets are included. | Empty cyst output concerns access to a supervised concept. |
| SAT-Pro | Yes | KiTS23 in SAT-DS | SAT-DS documentation and the released vocabulary list kidney tumor and kidney cyst separately. | Cyst/tumor confusion concerns supervised neighboring concepts. |
| SegVol | Yes | KiTS23 in the supervised 25-dataset mixture | The official supplementary dataset table lists kidney, kidney tumor, and kidney cyst for KiTS23. | Background-dominant output is not explained by absent cyst supervision. |
| Medical-SAM3 | Yes | BiomedSegFM `CT_KidneyTumor` subset | The released 3D configuration includes `CT_KidneyTumor`; the category inventory distinguishes left/right kidney cyst. | The checkpoint exposes a distinct cyst concept; exact upstream patient membership is unavailable. |
| BiomedParse v2 | Yes | CVPR BiomedSegFM 3D corpus | The v2 repository states that its 3D weights use BiomedSegFM and lists left/right kidney cyst as supported CT tasks. | Task support does not guarantee reliable retrieval; exact upstream patient membership is unavailable. |

## Primary sources

- VoxTell: <https://arxiv.org/abs/2511.11450> and
  <https://github.com/MIC-DKFZ/VoxTell>
- SAT and SAT-DS: <https://github.com/zhaoziheng/SAT> and
  <https://github.com/zhaoziheng/SAT-DS>
- SegVol: <https://arxiv.org/abs/2311.13385> and
  <https://github.com/BAAI-DCAI/SegVol>
- Medical-SAM3: <https://arxiv.org/abs/2601.10880> and
  <https://github.com/AIM-Research-Lab/Medical-SAM3>
- BiomedParse v2 and BiomedSegFM:
  <https://github.com/microsoft/BiomedParse/tree/v2> and
  <https://huggingface.co/datasets/junma/CVPR-BiomedSegFM>

## Scope

For checkpoints whose published mixtures include KiTS23 or a normalized renal
subset, KiTS23 is a training-source-domain audit. Without image-level training
manifests, it is not verified patient-level generalization.
