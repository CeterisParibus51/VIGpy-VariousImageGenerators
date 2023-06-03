import math
from PIL import Image, ImageDraw

def draw_polygon(sides):
    img_size = 400
    img_center = img_size // 2
    radius = img_size // 2 - 10

    # Calculate angle of each point in polygon
    angle = 2 * math.pi / sides

    # Calculate points of polygon
    points = []
    for i in range(sides):
        x = int(radius * math.cos(angle * i) + img_center)
        y = int(radius * math.sin(angle * i) + img_center)
        points.append((x, y))

    # Draw polygon on image
    img = Image.new("RGB", (img_size, img_size), "white")
    draw = ImageDraw.Draw(img)
    draw.polygon(points, outline="black")

    # Save image
    filename = f"polygon_{sides}.png"
    img.save(filename)
    print(f"{sides}-sided polygon saved as {filename}")

# Prompt user for number of sides
sides = int(input("Enter the number of sides for the polygon: "))

# Draw polygon and save as PNG
draw_polygon(sides)
