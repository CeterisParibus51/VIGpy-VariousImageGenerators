from PIL import Image, ImageDraw
import math

# Ask user for input angle in degrees
angle = int(input("Enter angle in degrees: "))

# Create image and drawing objects
img = Image.new('RGB', (400, 400), (255, 255, 255))
draw = ImageDraw.Draw(img)

# Calculate the end points of the lines
x1 = 200 + 100 * math.cos(math.radians(angle))
y1 = 200 + 100 * math.sin(math.radians(angle))
x2 = 200 + 100 * math.cos(math.radians(angle-angle))
y2 = 200 + 100 * math.sin(math.radians(angle+angle))

# Draw the lines on the image
draw.line((200, 200, x1, y1), fill=(0, 0, 0), width=3)
draw.line((200, 200, x2, y2), fill=(0, 0, 0), width=3)

# Export the image as a .png file
filename = "angle_" + str(angle) + ".png"
img.save(filename, "PNG")
