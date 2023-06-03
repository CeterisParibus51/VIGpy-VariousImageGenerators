from PIL import Image
import random

# Get user inputs
filename = input("Enter filename: ")
height = int(input("Enter height: "))
width = int(input("Enter width: "))

# Create a new image with random RGB values for each pixel
im = Image.new(mode='RGB', size=(width, height))
pixels = im.load()
for x in range(width):
    for y in range(height):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        pixels[x, y] = (r, g, b)

# Save the image to disk as a PNG
im.save(filename + '.png', 'PNG')
