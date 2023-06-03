from PIL import Image, ImageDraw
import math

# get number of points from user input
n = int(input("Enter the number of points for the star: "))

# calculate inner and outer radius of the star
r_in = 50
r_out = 100

# create new image
image = Image.new('RGB', (300, 300), color = 'white')

# create drawing object
draw = ImageDraw.Draw(image)

# calculate coordinates for points of the star
points = []
for i in range(n * 2):
    r = r_out if i % 2 == 0 else r_in
    x = math.cos(i * math.pi / n) * r + 150
    y = math.sin(i * math.pi / n) * r + 150
    points.append((x, y))

# draw the star
draw.polygon(points, fill='black')

# save the image
image.save(f'star{n}.png')
print(f'Saved star{n}.png')
