from PIL import Image, ImageDraw
import random

def random_shape(width, height):
    # create a new image and drawing context
    image = Image.new('RGBA', (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    # generate random polygon points
    points = []
    for i in range(5):
        x = random.randint(0, width)
        y = random.randint(0, height)
        points.append((x, y))

    # draw polygon with random color
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    draw.polygon(points, fill=color, outline=(0, 0, 0))

    # apply random transforms
    if random.random() < 0.5:
        image = image.transpose(Image.FLIP_LEFT_RIGHT)
    if random.random() < 0.5:
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
    if random.random() < 0.5:
        image = image.rotate(random.randint(0, 360))

    return image

def create_abstract_shapes(num_shapes, width, height, filename):
    # create a new image and drawing context
    image = Image.new('RGBA', (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    # generate random shapes and place them on the image
    for i in range(num_shapes):
        shape = random_shape(width, height)
        x = random.randint(0, width - shape.width)
        y = random.randint(0, height - shape.height)
        image.alpha_composite(shape, (x, y))

    # save the image
    image.save(filename)

# example usage
create_abstract_shapes(10, 500, 500, "abstract_shapes.png")
