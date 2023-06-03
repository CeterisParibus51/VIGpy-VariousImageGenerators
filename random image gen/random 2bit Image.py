from PIL import Image
import random

filename = input("Enter filename: ")
height = int(input("Enter height: "))
width = int(input("Enter width: "))

# Create a new image with random values for each pixel
img = Image.new('RGB', (width, height))
pixels = img.load()

for i in range(width):
    for j in range(height):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        pixels[i, j] = (r, g, b)

# Convert the image to black and white (2bit)
img = img.convert('1')

# Save the image
img.save(filename + ".png")
