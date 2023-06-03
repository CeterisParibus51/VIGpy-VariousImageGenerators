import re
from PIL import Image

# Load pixel data from input file
filename = "input-pixels.txt"
with open(filename, "r") as f:
    lines = f.readlines()
    total_x = int(lines[0].split(":")[1].strip())
    total_y = int(lines[1].split(":")[1].strip())
    pixel_data = []
    for line in lines[2:]:
        match = re.match(r"\((\d+),(\d+)\)\s+\((\d+),(\d+),(\d+)\)", line.strip())
        if match:
            x, y, r, g, b = match.groups()
            pixel_data.append((int(r), int(g), int(b)))
        else:
            print(f"Error: invalid pixel data format in line: {line}")

# Create new image and set pixel data
img = Image.new("RGB", (total_x, total_y))
img.putdata(pixel_data)

# Save output image to file
output_filename = f"{filename.split('.')[0]}.png"
img.save(output_filename)
