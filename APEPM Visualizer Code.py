import matplotlib.pyplot as plt
import re

# Please note: This code is purely for visualization of values calculated by (APEPM code implementation.py) specifically
# the overlap radius value.
# Licensed under: CC BY-NC 4.0

# This model was created by: Dylan M. Armstrong
# creator contact: halodma07@gmail.com

electron_cloud_radii = {'H': 1.30, 'He': 1.60, 'Li': 2.05, 'Be': 1.75, 'B': 2.15, 'C': 1.90, 'N': 1.75, 'O': 1.72, 'F': 0.85,
                        'Ne': 1.75, 'Na': 2.15, 'Mg': 1.85, 'Al': 2.10, 'Si': 2.35, 'P': 2.05, 'S': 2.05, 'Cl': 1.95, 'Ar': 2.10,
                        'K': 2.55, 'Ca': 2.20, 'Sc': 2.25, 'Ti': 2.35, 'V': 2.35, 'Cr': 2.35, 'Mn': 2.40, 'Fe': 2.40, 'Ni': 1.85,
                        'Co': 1.75, 'Cu': 1.60, 'Zn': 1.60, 'Ga': 2.10, 'Ge': 2.35, 'As': 2.10, 'Se': 2.20, 'Br': 2.05, 'Kr': 2.25,
                        'Rb': 2.65, 'Sr': 2.35, 'Y': 2.40, 'Zr': 2.55, 'Nb': 2.55, 'Mo': 2.55, 'Tc': 2.60, 'Ru': 2.60, 'Rh': 2.55,
                        'Pd': 1.95, 'Ag': 1.80, 'Cd': 1.80, 'In': 2.20, 'Sn': 2.35, 'Sb': 2.20, 'I': 2.20, 'Xe': 2.35, 'Cs': 2.80,
                        'Te': 2.25,  'Ba': 2.55, 'La': 2.40, 'Ce': 2.55, 'Pr': 2.55, 'Nd': 2.55, 'Pm': 2.60, 'Sm': 2.70, 'Eu': 2.75,
                        'Gd': 2.80, 'Tb': 2.85, 'Dy': 2.90, 'Ho': 2.90, 'Er': 2.95, 'Tm': 3.00, 'Yb': 3.05, 'Lu': 3.10, 'Hf': 2.60,
                        'Ta': 2.60, 'W': 2.60, 'Re': 2.70, 'Os': 2.70, 'Ir': 2.70, 'Pt': 1.95, 'Au': 1.65, 'Hg': 1.75, 'Tl': 2.20,
                        'Pb': 2.20, 'Bi': 2.30, 'Po': 2.30, 'At': 2.30, 'Rn': 2.40, 'Fr': 2.85, 'Ra': 2.60, 'Ac': 2.60, 'Th': 2.85,
                        'Pa': 2.85, 'U': 2.85, 'Np': 2.95, 'Pu': 2.95, 'Am': 3.05, 'Cm': 3.05, 'Bk': 3.15, 'Cf': 3.15, 'Es': 3.25,
                        'Fm': 3.25, 'Md': 3.25, 'No': 3.35, 'Lr': 3.35, 'Rf': 3.00, 'Db': 3.00, 'Sg': 3.00, 'Bh': 3.00, 'Hs': 3.00,
                        'Mt': 3.00, 'Ds': 3.00, 'Rg': 3.00, 'Cn': 3.00, 'Nh': 3.00, 'Fl': 3.00, 'Mc': 3.00, 'Lv': 3.00, 'Ts': 3.00,
                        'Og': 3.00}


input_bond = input("Please Enter Bond Here (e.g., O-H, C-O etc.): ")  # Only do 1 bond type at a time. Do not enter any numbers here
input_overlap_radius = float(input("Please Enter the Overlap Radius (Å): "))

# for the value that is needed in input_overlap_radius this will come from APEPM code implementation.py, and will be found
# in the list overlap_radius_list only enter the number of the bond you are trying to visualize for example in [{'O-H': 1.415794829768777}]
# enter 1.415794829768777

# Please note that the blue element is the first one from the bond string, and the second element will be red for example
# in O-H, O will be blue, and H will be red

# Parse bond elements
if "-" in input_bond:
    element1, element2 = input_bond.split("-")
else:
    elements = re.findall(r"[A-Z][a-z]*", input_bond)
    if len(elements) != 2:
        raise ValueError(f"Invalid bond format: {input_bond}")
    element1, element2 = elements
radius1 = electron_cloud_radii[element1]
radius2 = electron_cloud_radii[element2]

# Determine positions
# Nuclei are horizontally aligned: element1 at x=0, element2 at x determined by overlap
x1 = 0
x2 = radius1 + radius2 - input_overlap_radius  # distance between nuclei accounting for overlap
y = 0  # same horizontal line

# Create plot
fig, ax = plt.subplots()
ax.set_aspect('equal')

# Plot electron clouds (transparent)
cloud1 = plt.Circle((x1, y), radius1, color='blue', alpha=0.3, label=f'{element1} electron cloud')
cloud2 = plt.Circle((x2, y), radius2, color='red', alpha=0.3, label=f'{element2} electron cloud')
ax.add_artist(cloud1)
ax.add_artist(cloud2)

# Plot nuclei as dots
ax.plot(x1, y, 'bo', markersize=6, label=f'{element1} nucleus')
ax.plot(x2, y, 'ro', markersize=6, label=f'{element2} nucleus')

# Labels and aesthetics
ax.set_xlim(-radius1*1.5, x2 + radius2*1.5)
ax.set_ylim(-max(radius1, radius2)*1.5, max(radius1, radius2)*1.5)
ax.set_xlabel("X-axis (Å)")
ax.set_ylabel("Y-axis (Å)")
ax.set_title(f"Visualization of {input_bond} bond")
ax.legend(loc='upper right')
plt.grid(False)
plt.show()
