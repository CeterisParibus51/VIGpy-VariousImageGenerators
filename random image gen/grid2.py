#create a script that generates grids where cells have a specified number of sides as images
#Here's an example script that generates a grid where each cell has a specified number of sides and saves it as an image:
#python

import math
from PIL import Image, ImageDraw

# Prompt user for input
n = int(input("Enter number of sides per cell: "))
m = int(input("Enter number of cells per row/column: "))

# Set image size based on number of cells and cell size
cell_size = 50
width = height = m * cell_size

# Create new image and draw object
img = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(img)

# Draw grid lines
for i in range(m):
    for j in range(m):
        # Calculate cell coordinates
        x0 = j * cell_size
        y0 = i * cell_size
        x1 = x0 + cell_size
        y1 = y0 + cell_size

        # Draw cell
        draw.polygon([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], outline="black")

        # Draw sides of cell
        for k in range(n):
            angle = 2 * math.pi * k / n
            dx = cell_size / 2 * math.cos(angle)
            dy = cell_size / 2 * math.sin(angle)
            draw.line([(x0 + cell_size / 2 + dx, y0 + cell_size / 2 + dy), (x0 + cell_size / 2 - dx, y0 + cell_size / 2 - dy)], fill="black")

# Save image
filename = f"grid_{n}_sides_{m}_cells.png"
img.save(filename)

print(f"Saved image as {filename}")

#This script prompts the user for the number of sides per cell (n) and the number of cells per row/column (m), and generates an image where each cell has n sides. It saves the resulting image as a PNG file with a filename indicating the number of sides and cells.