# porous-diffusioin-isomap
## GitHub Repository Overview
This repository predicts the gas diffusion coefficient of unknown porous structures using Isomap method.The training dataset consists of the logarithmically transformed power-spectrum 3D voxel images (HDS (3-1)) obtained from 126 porous structures.The trained Isomap model is loaded and used to estimate the diffusion coefficient D_pred for a given test map.The test map must be provided as TIFF images of 3D image slices (HDS (1-1)).The conversion to the logarithmic power spectrum is performed automatically.

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

```text
.
├── LICENSE
├── requirements.txt
├── demo/
│   ├── run_codes.sh          # Master script that executes the workflow
│   ├── code_Isomap.py        # Computes the Isomap embedding. Loads model.pkl and a test map, then performs the transform
│   ├── code_pred.py          # Finds the nearest training map and predicts D_pred
│   ├── helpers.py            # Helper functions and utilities
│   │
│   ├── model/
│   │   ├── model.pkl         # Trained Isomap model (HDS (3-1))
│   │   ├── list_model.txt    # Parameter list of the training dataset
│   │   ├── Eigenvector-1.txt # First Isomap coordinate of the training dataset
│   │   ├── Diff_data.txt     # Diffusion coefficients of the training dataset
│   │   └── Mean_data.txt     # Mean particle diameters of the training dataset
│   │
│   ├── testmap/
│   │   └── data_1/
│   │       └── normalZ*.tif  # 3D image slices (HDS (1-1)) for testing
│   │
│   └── results/
│       └── data_1/
│           ├── data_1.txt            # Low-dimensional embedding obtained by Isomap method for the test map
│           ├── prediction.txt        # D_pred and parameters of the nearest training map
│           └── E1_vs_Porespy_D_m.png # Visualization of prediction (cross indicates nearest training map)
```

## Usage
### Using default sample
To run the code:
```text
cd demo/
bash run_codes.sh
```
The prepared sample dataset located in ```testmap/data_1/``` is used, and the predicted gas diffusion coefficient is saved to:
```text
results/data_1/
```

### Using default sample
To predict a different sample, edit run_codes.sh and change:
```text
path_testmap="data_1"
```
to your dataset name.Then place your 3D image slices in:
```text
testmap/<path_testmap>/
```
using the same format as the default sample. After execution, the prediction results will be generated in:
```text
results/<path_testmap>/
```
Input image requirements
- `TIFF image stack (3D slices)`
- `Solid phase: 255`
- `Pore phase: 0`

# Licence
This project is licensed under the MIT License.

# Citing this work
If you use "PorousGen", please cite:
```
Shota. Arai, Yuki Takayama, and Takashi. Yoshidome,
Structure-based Prediction of Gas Diffusion Property of Catalytic Layer of Proton Exchange Membrane Fuel Cells via Manifold Learning and X-ray Ptychographic Nano-computed Tomography,
J. Power. Sources., XXX (2026), XXXXXX, 
https://doi.org/XXX
```

# Contact
If you have any questions, please contact Takashi Yoshidome at<br>
takashi.yoshidome.b1@tohoku.ac.jp <br>
or Shota Arai at<br>
shota.arai.c2@tohoku.ac.jp
