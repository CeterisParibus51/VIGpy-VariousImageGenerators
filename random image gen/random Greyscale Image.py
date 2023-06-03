from PIL import Image
import random

# Ask user for filename, height, and width
filename = input("Enter a filename: ")
height = int(input("Enter the height of the image: "))
width = int(input("Enter the width of the image: "))

# Generate a new image with random RGB values
new_image = Image.new('RGB', (width, height))
pixels = new_image.load()
for x in range(width):
    for y in range(height):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        pixels[x, y] = (r, g, b)

# Convert image to grayscale
new_image = new_image.convert('L')

# Save the image
new_image.save(filename + ".png")
print("Image saved as " + filename + ".png")
