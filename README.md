# porous-diffusioin-isomap
## GitHub Repository Overview
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

## Folder Structure
.
├── LICENSE
├── requirements.txt
├── demo/
│   ├── run_codes.sh          : Master script that executes the following programs
│   ├── code_Isomap.py        : Computes the Isomap embedding. 
│   │                             Loads model.pkl and a test map, and performs the transform.
│   ├── code_pred.py          : Finds the nearest training map and predicts Dpred
│   ├── helpers.py            : Helper functions and utilities
│   │
│   ├── model/
│   │   ├── model.pkl         : Trained Isomap model (HDS (3-1))
│   │   ├── list_model.txt    : Parameter list of training dataset
│   │   ├── Eigenvector-1.txt : First Isomap coordinates of training dataset
│   │   ├── Diff_data.txt     : Diffusion coefficients of training dataset
│   │   └── Mean_data.txt     : Mean particle diameter of training dataset
│   │
│   ├── testmap/
│   │   └── data_1/
│   │       └── normalZ*.tif  : 3D image slices (HDS (1-1)) for testing
│   │
│   └── results/
│       └── data_1/                     : Output directory containing prediction results
│           ├── data_1.txt              : LDS obtained by Isomap method for the test data
│           ├── prediction.txt          : Dpred and the parameters of the nearest training map
│           └── E1_vs_Porespy_D_m.png   : Visualization of prediction (the cross symbol indicates the nearest training sample)
