from PIL import Image, ImageDraw
import math

# Ask user for input
num_circles = int(input("Enter the number of circles: "))
num_divisions = int(input("Enter the number of divisions: "))
padding = int(input("Enter the padding size: "))

# Create image and drawing objects
img = Image.new('RGB', (400, 400), (255, 255, 255))
draw = ImageDraw.Draw(img)

# Calculate circle radii and draw circles
for i in range(num_circles):
    radius = (i+1) * (padding + 20)  # 20 is the default diameter of the circle
    draw.ellipse((200-radius, 200-radius, 200+radius, 200+radius), outline=(0, 0, 0))

# Draw dividing lines
for i in range(num_divisions):
    angle = i * (360/num_divisions)
    x1 = 200 + (num_circles * (padding + 20)) * math.cos(math.radians(angle))
    y1 = 200 + (num_circles * (padding + 20)) * math.sin(math.radians(angle))
    x2 = 200 + ((num_circles + 1) * (padding + 20)) * math.cos(math.radians(angle))
    y2 = 200 + ((num_circles + 1) * (padding + 20)) * math.sin(math.radians(angle))
    draw.line((x1, y1, x2, y2), fill=(0, 0, 0), width=3)

# Export the image as a .png file
filename = "concentric_circles.png"
img.save(filename, "PNG")
