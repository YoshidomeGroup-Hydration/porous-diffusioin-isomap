##########################################################
# read tiff
##########################################################
from PIL import Image
import numpy as np
from scipy.fftpack import fftn

VN = 500
def read_testmap(
        path_testmap
    ):

    volume = []

    for n in range(1, VN+1):
        with Image.open(f"{path_testmap}/normalZ{n:05d}.tif") as img:
            volume.append(np.array(img))

    volume = np.stack(volume) 
    g = fftn(volume)
    DP_3d = np.abs(g) ** 2
    DP_3d = np.log(DP_3d+1) 
    testmap = DP_3d.ravel()[None, :]
    return testmap    

