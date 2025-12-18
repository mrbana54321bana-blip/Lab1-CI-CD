import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = -8*X + 4*Y

theta = np.linspace(0, 2*np.pi, 400)
r = (17 / (np.cos(theta)**4 + np.sin(theta)**4))**(1/4)
x_line = r * np.cos(theta)
y_line = r * np.sin(theta)
z_line = -8*x_line + 4*y_line

min_idx = np.argmin(z_line)
max_idx = np.argmax(z_line)
min_pt = (x_line[min_idx], y_line[min_idx], z_line[min_idx])
max_pt = (x_line[max_idx], y_line[max_idx], z_line[max_idx])

fig = plt.figure(figsize=(12, 16))

ax1 = fig.add_subplot(2, 1, 1, projection='3d')

surf = ax1.plot_surface(X, Y, Z, cmap='viridis', alpha=0.6, edgecolor='none')

ax1.plot(x_line, y_line, z_line, color='black', linewidth=3, label='Constraint Path')

ax1.scatter(*max_pt, color='red', s=100, label=f'Max ({z_line[max_idx]:.1f})', zorder=10)
ax1.scatter(*min_pt, color='blue', s=100, label=f'Min ({z_line[min_idx]:.1f})', zorder=10)

ax1.set_title('3D: Цільова функція з накладеним обмеженням', fontsize=14)
ax1.set_xlabel('$x_1$')
ax1.set_ylabel('$x_2$')
ax1.set_zlabel('$f_0$')
ax1.legend()
ax1.view_init(elev=25, azim=-60)

ax2 = fig.add_subplot(2, 1, 2)

contour_filled = ax2.contourf(X, Y, Z, levels=20, cmap='YlOrBr')
fig.colorbar(contour_filled, ax=ax2, label='Значення $f_0$')

ax2.plot(x_line, y_line, color='dodgerblue', linewidth=3, label='$x_1^4 + x_2^4 = 17$')

ax2.scatter(max_pt[0], max_pt[1], color='red', s=80, zorder=5, edgecolors='black')
ax2.scatter(min_pt[0], min_pt[1], color='blue', s=80, zorder=5, edgecolors='black')

ax2.set_title('2D: Лінії рівня та межа допустимої області', fontsize=14)
ax2.set_xlabel('$x_1$')
ax2.set_ylabel('$x_2$')
ax2.legend()
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.set_aspect('equal')

plt.tight_layout()
plt.show()