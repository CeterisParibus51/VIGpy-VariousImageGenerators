import random
from PIL import Image

filename = input("Enter filename: ")
height = int(input("Enter height: "))
width = int(input("Enter width: "))

im = Image.new("RGBA", (width, height), (0, 0, 0, 0))

for x in range(width):
    for y in range(height):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        a = random.randint(0, 255)
        im.putpixel((x, y), (r, g, b, a))

im.save(f"{filename}.png")
