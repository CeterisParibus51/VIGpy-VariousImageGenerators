from PIL import Image
import random

# Define image size and color depth
WIDTH = 256
HEIGHT = 256
DEPTH = 8

# Create a new image with a white background
img = Image.new('L', (WIDTH, HEIGHT), color=255)

# Define the dither pattern
pattern = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]

# Generate random pixel values
for y in range(HEIGHT):
    for x in range(WIDTH):
        px_value = random.randint(0, (2**DEPTH)-1)
        img.putpixel((x, y), px_value)

# Apply the dither pattern
for y in range(HEIGHT):
    for x in range(WIDTH):
        old_value = img.getpixel((x, y))
        new_value = old_value + pattern[y % 4][x % 4]
        img.putpixel((x, y), new_value)

# Save the image as a PNG file
img.save('dither.png')
