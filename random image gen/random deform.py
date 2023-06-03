from PIL import Image, ImageDraw
import random

# Define the shape
width, height = 500, 500
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

# Draw the shape
shape = [(100, 100), (200, 100), (200, 200), (100, 200)]
draw.polygon(shape, fill='black')

# Randomly deform the shape
num_deformations = 10
for i in range(num_deformations):
    x, y = random.randint(-10, 10), random.randint(-10, 10)
    shape = [(x + p[0], y + p[1]) for p in shape]
    draw.polygon(shape, fill='black')

# Save the image
image.save('deformed_shape.png')
