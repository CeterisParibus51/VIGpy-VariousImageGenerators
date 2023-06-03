from PIL import Image
import random

# user input for width and height
width = int(input("Enter width: "))
height = int(input("Enter height: "))

# create new image
im = Image.new("RGB", (width, height))

# iterate through each pixel and randomly set the color
for y in range(height):
    for x in range(width):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        im.putpixel((x, y), (r, g, b))

# save the image as a PNG file
im.save("random_pattern.png")
