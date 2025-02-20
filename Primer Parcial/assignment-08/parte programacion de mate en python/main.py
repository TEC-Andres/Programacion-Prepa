"""
#       Sesión 10: Assignment-08
#       Andrés Rodríguez Cantú ─ A01287002
#
#       Copyright (C) Tecnológico de Monterrey
#
#       Archivo: main.py
#
#       Creado:                   20/02/2024
#       Última Modificación:      20/02/2024
"""

import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt

def get_border_points(image_path, num_points=100):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    image = cv2.GaussianBlur(image, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY_INV, 11, 2)

    kernel = np.ones((3, 3), np.uint8)
    thresh = cv2.dilate(thresh, kernel, iterations=1)
    thresh = cv2.erode(thresh, kernel, iterations=1)

    edges = cv2.Canny(thresh, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if not contours:
        print("No contours found!")
        return []

    all_points = np.vstack(contours).squeeze()
    unique_points = np.unique(all_points, axis=0)
    indices = np.linspace(0, len(unique_points) - 1, num_points, dtype=int)
    sampled_points = unique_points[indices]

    return sampled_points.tolist()

def plot_image_with_points(image_path, points):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    plt.imshow(image, cmap="gray")
    plt.scatter(*zip(*points), c='red', s=10)
    plt.show()

def select_image_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")]
    )
    return file_path

# Main Execution
image_path = select_image_file()
if image_path:
    points = get_border_points(image_path, num_points=100) # Number of points
    for i in points:
        print(i)
    plot_image_with_points(image_path, points)
else:
    print("No image selected.")
