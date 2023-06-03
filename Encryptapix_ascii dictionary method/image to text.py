from PIL import Image
import numpy as np

# Load input PNG image and extract size in pixels
filename = "input.png"
try:
    img = Image.open(filename)
    total_x, total_y = img.size
except FileNotFoundError:
    print(f"Error: file {filename} not found")
    exit()
except Exception as e:
    print(f"Error: {e}")
    exit()

# Convert image to RGB mode
if img.mode != "RGB":
    img = img.convert("RGB")

# Convert image to NumPy array and extract RGB values per pixel
pixels = np.array(img)
pixel_data = []
for x in range(total_x):
    for y in range(total_y):
        pixel = pixels[y][x]
        r, g, b = pixel
        pixel_data.append((x, y, r, g, b))

# Write output to text file in desired format
output_filename = f"{filename}-pixels.txt"
with open(output_filename, "w") as f:
    f.write(f"Total X : {total_x}\n")
    f.write(f"Total Y : {total_y}\n")
    for data in pixel_data:
        x, y, r, g, b = data
        f.write(f"({x},{y}) ({r},{g},{b})\n")
