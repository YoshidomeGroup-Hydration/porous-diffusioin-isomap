import os
import sys
import numpy as np            

load_testmap = sys.argv[1]
path_testmap = f"testmap/{load_testmap}"

output_directory = f"results/{load_testmap}"
os.makedirs(output_directory, exist_ok=True)
print(output_directory)


Eigenvector1 = np.loadtxt(f'model/Eigenvector-1.txt')
transformed_add = np.loadtxt(f'results/{load_testmap}/{load_testmap}.txt')
if transformed_add.ndim == 1:
    transformed_add = transformed_add.reshape(1, -1)
Eigenvector1_add_point = transformed_add[:, 0]

list_model = np.loadtxt(f'model/list_model.txt', dtype=str)
classes_m = np.loadtxt(f'model/Mean_data.txt')
Porespy_D = np.loadtxt(f'model/Diff_data.txt')
#Porespy_D = Porespy_D.reshape(1, -1)
Porespy_D = 1/Porespy_D[:,0]

absolute_diff = np.abs(Eigenvector1 - Eigenvector1_add_point)
nearest_index = np.argmin(absolute_diff)
 
print('Dpred:', 1/Porespy_D[nearest_index])
print('parameter:', list_model[nearest_index])

result_path = os.path.join(output_directory, "prediction.txt")
with open(result_path, "w") as f:
    f.write(f"Dpred: {1/Porespy_D[nearest_index]}\n")
    f.write(f"parameter: {list_model[nearest_index]}\n")


################################################################
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import ScalarFormatter

mpl.rcParams.update({
    "font.size": 24,
    "axes.labelsize": 24,
    "xtick.labelsize": 24,
    "ytick.labelsize": 24,
    "axes.titlesize": 24,
    "legend.fontsize": 24,
    # marker settings
    "lines.markersize": 10,
    "lines.markeredgewidth": 2,
})

class_mapping_m = {
    (40, 50): 'gray',
    (50, 60): 'silver',
    (60, 70): 'lightcoral',
    (70, 80): 'maroon',
    (80, 90): 'orangered',
    (90, 100): 'chocolate',
    (100, 110): 'goldenrod',
    (110, 120): 'greenyellow',
    (120, 130): 'darkgreen',
    (130, 140): 'mediumseagreen',
    (140, 150): 'mediumturquoise',
    (150, 160): 'aqua',
    (160, 170): 'powderblue',
    (170, 180): 'mediumblue',
    (180, 190): 'darkorchid',
    (190, 200): 'plum',
}
################################################################
def setup_xaxis(ax):
    # Configure x-axis with scientific notation
    ax.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
    ax.ticklabel_format(style="sci", axis="x", scilimits=(0, 0))
    # Adjust font size
    ax.tick_params(axis='both', which='major')
    offset = ax.xaxis.get_offset_text()
    offset.set_x(1.02)
    offset.set_y(-0.02)        
    offset.set_ha('left')
    offset.set_va('top')

def setup_yaxis_Diff(ax):
    # Get current y-axis ticks
    yticks = ax.get_yticks()

    # Set y-axis tick positions using FixedLocator
    ax.yaxis.set_major_locator(ticker.FixedLocator(yticks))

    # Set y-axis tick labels scaled by 10^6 using FixedFormatter
    ax.yaxis.set_major_formatter(
       # ticker.FixedFormatter([f"{tick * 10**6:.1f}" for tick in yticks])
       ticker.FixedFormatter([f"{tick :.2f}" for tick in yticks])
    )

    # Adjust font size for tick labels
    ax.tick_params(axis='both', which='major')
################################################################
fig, ax = plt.subplots(constrained_layout=True)
for (start, end), color in class_mapping_m.items():
    indices = np.where((classes_m >= start) & (classes_m < end))[0]
    ax.scatter(Eigenvector1[indices], Porespy_D[indices], c=color, marker='o', label=f'{start}-{end}')
    ax.scatter(Eigenvector1[nearest_index], Porespy_D[nearest_index], c='black', marker='x', label=f'{start}-{end}')
    #ax.scatter(Eigenvector1_add_point, Porespy_D_add, c='black', marker='*', label=f'{start}-{end}')
setup_xaxis(ax)  
setup_yaxis_Diff(ax)
ax.set_xlabel("Eigenvectors 1")
ax.set_ylabel(r"$D_{\mathrm{H}}$")
plt.savefig(os.path.join(output_directory, 'E1_vs_Diff.png'))
plt.close()

