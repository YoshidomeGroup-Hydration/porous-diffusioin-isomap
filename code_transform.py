
import os
import sys
import numpy as np            
from sklearn.manifold import Isomap
from helpers import read_testmap
import joblib

load_model = sys.argv[1]
load_testmap = sys.argv[2]
path_testmap = f"testmap/{load_testmap}"

output_directory = f"results/{load_testmap}"
os.makedirs(output_directory, exist_ok=True)
print(output_directory)

isomap = joblib.load(load_model)
testmap = read_testmap(path_testmap)
print("testmap shape:", testmap.shape)
print("model expects:", isomap.n_features_in_)
transformed_add_data = isomap.transform(testmap)
np.savetxt(os.path.join(output_directory, f'{load_testmap}.txt'), transformed_add_data)