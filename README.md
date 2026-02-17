# porous-diffusioin-isomap
# GitHub Repository Overview
This repository predicts the gas diffusion coefficient of unknown porous structures using Isomap method.The training dataset consists of the logarithmically transformed power-spectrum 3D voxel images (HDS (3-1)) obtained from 126 porous structures.The trained Isomap model is loaded and used to estimate the diffusion coefficient Dpred for a given test map.The test map must be provided as TIFF images of 3D image slices (HDS (1-1)).The conversion to the logarithmic power spectrum is performed automatically.

## Requirements
Python **3.12.3** or later
- numpy  (version 2.1.3)
- scipy  (version 1.15.2)
- scikit-learn (version 1.6.1)   
- joblib (version 1.4.2)
- Pillow (version: 11.0.0)
- matplotlib (version: 3.10.0)

Install dependencies:

```bash
pip install -r requirements.txt
```
