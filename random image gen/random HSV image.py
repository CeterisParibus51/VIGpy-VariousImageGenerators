import random
import colorsys
from PIL import Image

# Ask the user for input
filename = input("Enter filename (without extension): ")
width = int(input("Enter width in pixels: "))
height = int(input("Enter height in pixels: "))

# Create a new image with the given dimensions
image = Image.new("RGBA", (width, height))

# Loop through each pixel in the image
for x in range(width):
    for y in range(height):
        # Generate a random hue, saturation, and value
        h = random.random()
        s = random.random()
        v = random.random()
        
        # Convert HSV to RGB
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        
        # Set the pixel color
        image.putpixel((x, y), (int(r*255), int(g*255), int(b*255), 255))

# Save the image
image.save(filename + ".png")
print("Image saved as " + filename + ".png")
