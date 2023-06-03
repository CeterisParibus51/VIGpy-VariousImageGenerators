import random
from PIL import Image, ImageDraw

# user-defined parameters
width = 500
height = 500
num_shapes = 10
max_shape_size = 100

# create an empty image
image = Image.new("RGB", (width, height), color=(255, 255, 255))

# draw shapes on the image
draw = ImageDraw.Draw(image)
for i in range(num_shapes):
    # choose a random color
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # choose a random shape size and position
    shape_size = random.randint(10, max_shape_size)
    x = random.randint(0, width - shape_size)
    y = random.randint(0, height - shape_size)

    # draw the shape
    draw.rectangle([(x, y), (x + shape_size, y + shape_size)], fill=color)

# save the image as a PNG
image.save("abstract.png", "PNG")
