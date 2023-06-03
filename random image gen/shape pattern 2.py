import random
from PIL import Image, ImageDraw, ImageColor

# Define the size of the image and the number of shapes
img_size = (500, 500)
num_shapes = 10

# Define the size range and color range of the shapes
min_shape_size = 10
max_shape_size = 100
min_shape_color = '#000000'
max_shape_color = '#FFFFFF'

# Define the range of the random offset for each shape
offset_range = 50

# Create the new image
img = Image.new('RGB', img_size, '#FFFFFF')

# Draw the shapes on the image
draw = ImageDraw.Draw(img)
for i in range(num_shapes):
    # Randomly choose the size and color of the shape
    shape_size = random.randint(min_shape_size, max_shape_size)
    shape_color = ImageColor.getrgb(random.choice([min_shape_color, max_shape_color]))
    
    # Randomly choose the position and offset of the shape
    pos = (random.randint(0, img_size[0] - shape_size), random.randint(0, img_size[1] - shape_size))
    offset = (random.randint(-offset_range, offset_range), random.randint(-offset_range, offset_range))
    shape_pos = (pos[0] + offset[0], pos[1] + offset[1])
    
    # Draw the shape on the image
    draw.ellipse((shape_pos[0], shape_pos[1], shape_pos[0] + shape_size, shape_pos[1] + shape_size), fill=shape_color)

# Save the image as a PNG file
img.save('random_shapes.png')
