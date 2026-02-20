
import os
import sys
import numpy as np            
from sklearn.manifold import Isomap
from scipy.fftpack import fftn
import joblib

load_list = sys.argv[1]
path_model = sys.argv[2]

N = 126
V = 500**3

maps = np.zeros((N, V))


with open(f"{load_list}.txt") as f:
    names = [line.strip() for line in f if line.strip()]

for i, name in enumerate(names):

    path = os.path.join("train_data/", f"{name}.npz")
    print("processing:", path)

    # --- load map ---
    map = np.load(path)["data"]

    # --- FFT ---
    F = np.fft.fftn(map)
    I = np.abs(F)**2
    I = np.log(I + 1.0)
    maps[i] = I.ravel()
    del map, F, I


isomap = Isomap(n_neighbors=5, n_components=10)
isomap.fit(maps)
joblib.dump(isomap, path_model)


