"""
#       Sesión 10: Assignment-08
#       Andrés Rodríguez Cantú ─ A01287002
#
#       Copyright (C) Tecnológico de Monterrey
#
#       Archivo: testpiecewise.py.py
#
#       Creado:                   20/02/2024
#       Última Modificación:      20/02/2024
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import sympy as sp

# Given points
points = [
(0, 0),(0.1336809037, 0.8117651834),(0.3208341688, 1.217647775),(0.6149321569, 1.589706817),(0.9625025065, 2.705883945),(1.203128133, 3.145590086),(1.764587929, 3.788237522),(2.486464809, 4.160296565),(3.235077869, 4.160296565),(4.01042711, 4.464708509),(4.785776352, 4.464708509),(5.534389412, 4.160296565),(6.309738654, 4.058825917),(7.085087895, 3.788237522),(7.833700956, 3.551472677),(8.609050197, 3.855884621),(9.357663258, 3.788237522),(10.1330125, 3.957355269),(10.90836174, 4.295590762),(11.6569748, 4.227943663),(12.43232404, 4.295590762),(13.20767328, 4.498532058),(13.95628634, 4.295590762),(14.73163559, 4.498532058),(15.50698483, 4.498532058),(16.25559789, 4.363237861),(17.03094713, 4.532355607),(17.80629637, 4.566179157),(18.55490943, 4.39706141),(19.33025867, 4.600002706),(20.07887173, 4.430884959),(20.85422097, 4.39706141),(21.62957022, 4.39706141),(22.37818328, 3.92353172),(23.04658779, 3.855884621),(23.55457523, 3.314707832),(24.11603502, 2.875001691),(24.704231, 2.198530705),(25.34589934, 1.725001015),(26.01430386, 1.45441262),(26.76291692, 1.116177127),(27.53826616, 0.9470593806),(28.28687922, 0.6426474369),(28.74139429, 1.150000676),(29.46327117, 1.116177127),(30.23862041, 1.082353578),(30.80008021, 0.7102945355)]

# Extract x and y coordinates
x_values, y_values = zip(*points)

# Fit a cubic spline
cs = CubicSpline(x_values, y_values)

# Generate x values for smooth curve
x_curve = np.linspace(min(x_values), max(x_values), 1000)
y_curve = cs(x_curve)

# Plot points and cubic spline curve
plt.figure(figsize=(10, 6))
plt.scatter(x_values, y_values, color='red', label="Original Points")
plt.plot(x_curve, y_curve, color='blue', linewidth=2, label="Cubic Spline Interpolation")

# Labels and legend
plt.xlabel("X")
plt.ylabel("Y")
plt.ylim(-50, 50)
plt.title("Cubic Spline Interpolation Through Given Points")
plt.legend()
plt.grid()

# Show plot
plt.show()

# Convert spline to sympy expression (piecewise)
x = sp.symbols('x')
splines = cs.c
knots = cs.x
piecewise_expr = sp.Piecewise(
    *[(sum(sp.Rational(c) * (x - knots[i])**j for j, c in enumerate(cs.c[:, i][::-1])), 
       (x >= knots[i]) & (x < knots[i+1])) for i in range(len(knots) - 1)]
)

# Print piecewise polynomial in LaTeX format
latex_piecewise = sp.latex(piecewise_expr)
print(f"The piecewise polynomial function in LaTeX format is:\n{latex_piecewise}")
print(f"The piecewise polynomial function is:\n{piecewise_expr}")
