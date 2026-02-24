# porous-diffusioin-isomap
## GitHub Repository Overview
This repository predicts the gas diffusion coefficient of unknown porous structures using Isomap method. The training dataset consists of the logarithmically transformed power-spectrum 3D voxel images (HDS (3-1)) obtained from 126 porous structures. The trained Isomap model is loaded and used to estimate the diffusion coefficient D_pred for a given test map. The test map must be provided as TIFF images of 3D image slices (HDS (1-1)). The conversion to the logarithmic power spectrum is performed automatically.

## Requirements
This code was tested with:

- Python 3.12.3
- numpy==2.1.3
- scipy==1.15.2
- scikit-learn==1.6.1
- joblib==1.4.2
- Pillow==11.0.0

Install dependencies:

```bash
pip install -r requirements.txt
```

## Folder Structure

```text
.
├── LICENSE
├── README.md
├── requirements.txt
├── demo/
│   ├── run_codes.sh          # Master script that executes the workflow
│   ├── code_make_model.py    # Builds model.pkl from 126 porous maps (training dataset)
│   ├── code_transform.py     # Computes the Isomap embedding. Loads model.pkl and a test map, then performs the transform
│   ├── code_pred.py          # Finds the nearest training map and predicts D_pred
│   ├── helpers.py            # Helper functions and utilities
│   │
│   ├── train_data/           # Training dataset downloaded from Zenodo
│   │   └── ran1_meanX_stanY_phi67.npz  
│   │
│   ├── model/
│   │   ├── model.pkl         # Trained Isomap model (HDS (3-1)); created by running code_make_model.py using the training dataset
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
│           └── prediction.txt        # D_pred and parameters of the nearest training map
```

## Usage
### 1. Download the training dataset
Because the trained model file (model.pkl, ~120 GB) exceeds the upload capacity of Zenodo, we instead provide the t**training dataset** required to reconstruct the model.

Please download the dataset from the Zenodo URL below and place it in`demo/train_data/`.

*https://zenodo.org/records/18752930*

### 2. Build the Isomap model
Run the following command:
```bash
cd demo/
bash run_codes.sh
```

After execution, the trained model will be generated:
```text
demo/model/model.pkl
```
Once the model is successfully created, edit `run_codes.sh`:
- Comment out `code_make_model.py`
- Uncomment `code_transform.py` and `code_pred.py`

### 3. Using default sample
To run the code:
```text
cd demo/
bash run_codes.sh
```
The prepared sample dataset located in ```testmap/data_1/``` is used, and the predicted gas diffusion coefficient is saved to:
```text
results/data_1/
```

### 4. Using your own sample
To predict a different sample, edit run_codes.sh and change:
```text
path_testmap="data_1"
```
to your dataset name. Then place your 3D image slices in:
```text
testmap/<path_testmap>/
```
using the same format as the default sample. After execution, the prediction results will be generated in:
```text
results/<path_testmap>/
```
### Input Image Requirements
The input data must be a stack of 2D TIFF slices representing a 3D binary porous structure.
- Voxel resolution: 10 nm
- Volume size: 500 × 500 × 500 voxels
- Solid phase intensity: 255
- Pore phase intensity: 0


# Licence
This project is licensed under the MIT License.

# Citing this work
If you use this code in your research, please cite the following work:
```
Shota Arai, Yuki Takayama, and Takashi Yoshidome,
Structure-based Prediction of Gas Diffusion Property of Catalytic Layer of Proton Exchange Membrane Fuel Cells via Manifold Learning and X-ray Ptychographic Nano-computed Tomography,
J. Power. Sources., XXX (2026), XXXXXX, 
https://doi.org/XXX
```

# Contact
If you have any questions, please contact Shota Arai at<br>
shota.arai.c2@tohoku.ac.jp
or Takashi Yoshidome at<br>
takashi.yoshidome.b1@tohoku.ac.jp <br>
