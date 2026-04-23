import numpy as np
import matplotlib.pyplot as plt
import os

# Set up figure
fig, ax = plt.subplots(figsize=(6, 6))

# Plot lattice of 2 * Z[\sqrt{-5}]
# Lattice points are 2(a + b \sqrt{-5}) = 2a + 2b \sqrt{-5}
A = np.arange(-3, 4)
B = np.arange(-2, 3)
sqrt5 = np.sqrt(5)

lattice_x = []
lattice_y = []
for a in A:
    for b in B:
        lattice_x.append(2*a)
        lattice_y.append(2*b*sqrt5)

ax.scatter(lattice_x, lattice_y, color='blue', s=30, label='$2\mathbb{Z}[\sqrt{-5}]$ (multiples de 2)')

# Plot Euclidean balls of radius 2 around each lattice point
# Since norm N(x+iy) = x^2 + 5y^2 = 4 for Euclidean division, it's a circle of radius 2 in actual Cartesian plane if we map x -> x, y -> y \sqrt{5}
# But distance squared is literally (Re)^2 + (Im)^2 = (2a)^2 + (2b\sqrt{5})^2.
# Wait! Norm in Z[\sqrt{-5}] is defined as N(a+b\sqrt{-5}) = a^2 + 5b^2.
# So if we map a+b i\sqrt{5} to Cartesian (a, b\sqrt{5}), the square distance corresponds exactly to the Norm!
# Thus the condition N(z - 2q) < N(2) = 4 means distance in Cartesian plane < 2 !
# We draw circles of radius 2 around the lattice points!

for cx, cy in zip(lattice_x, lattice_y):
    circle = plt.Circle((cx, cy), 2, color='blue', alpha=0.15)
    ax.add_patch(circle)

# Now, plot the point 1 + \sqrt{-5}
target_x = 1
target_y = sqrt5
ax.scatter([target_x], [target_y], color='red', s=60, zorder=5, label='$1 + i\sqrt{5}$')

# Add text to point
ax.text(target_x + 0.2, target_y + 0.2, '$1 + i\sqrt{5}$', color='red', fontsize=12)

# Annotations
ax.set_aspect('equal')
ax.set_xlim(-4.5, 4.5)
ax.set_ylim(-3.5 * sqrt5, 3.5 * sqrt5)
ax.set_xlabel('Re')
ax.set_ylabel('Im')
ax.set_title("Échec de la division euclidienne dans $\mathbb{Z}[i\sqrt{5}]$\n"
             "Le point rouge n'est couvert par aucun disque de rayon $N(2)=4$", fontsize=11)
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(loc='lower right')

# Save
output_path = '/home/gonenc/projects/mat205/private/mat205/source/tex/notes/z_sqrt5_lattice.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Saved to {output_path}")
