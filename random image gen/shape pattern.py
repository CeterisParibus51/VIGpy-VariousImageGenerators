import random
from PIL import Image, ImageDraw

# Define the size of the pattern
width = 300
height = 300

# Define the size and color range of the shapes
shape_size_range = (10, 50)
color_range = ((0, 0, 0), (255, 255, 255))

# Define the number of shapes to use in the pattern
num_shapes = 10

# Create a blank image to draw the pattern on
pattern = Image.new('RGB', (width, height), color_range[0])

# Define the drawing context
draw = ImageDraw.Draw(pattern)

# Define a list of shapes
shapes = ['rectangle', 'circle']

# Choose a random shape and draw it repeatedly in random locations and colors
for i in range(num_shapes):
    shape = random.choice(shapes)
    color = tuple(random.randint(color_range[0][j], color_range[1][j]) for j in range(3))
    size = random.randint(shape_size_range[0], shape_size_range[1])
    x = random.randint(0, width - size)
    y = random.randint(0, height - size)
    if shape == 'rectangle':
        draw.rectangle((x, y, x + size, y + size), fill=color)
    elif shape == 'circle':
        draw.ellipse((x, y, x + size, y + size), fill=color)

# Save the pattern as a png
pattern.save('random_pattern.png')
