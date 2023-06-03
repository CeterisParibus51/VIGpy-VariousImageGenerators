from PIL import Image, ImageDraw
import random

# Define image size and background color
size = (500, 500)
bg_color = (255, 255, 255, 255) # RGBA format, white color

# Create image object and drawing context
img = Image.new("RGBA", size, bg_color)
draw = ImageDraw.Draw(img)

# Define random shape parameters
x1, y1 = random.randint(0, size[0]), random.randint(0, size[1])
x2, y2 = random.randint(0, size[0]), random.randint(0, size[1])
x3, y3 = random.randint(0, size[0]), random.randint(0, size[1])
fill_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255) # RGBA format, random color

# Draw random shape
shape_type = random.choice(["rectangle", "triangle", "circle"])
if shape_type == "rectangle":
    draw.rectangle([x1, y1, x2, y2], fill=fill_color)
elif shape_type == "triangle":
    draw.polygon([(x1, y1), (x2, y2), (x3, y3)], fill=fill_color)
elif shape_type == "circle":
    draw.ellipse([x1, y1, x2, y2], fill=fill_color)

# Save image to file
img.save("random_shape.png")
