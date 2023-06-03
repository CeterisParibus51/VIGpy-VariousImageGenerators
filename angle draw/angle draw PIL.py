from PIL import Image, ImageDraw
import math

# Ask user for input angle in degrees
angle = int(input("Enter angle in degrees: "))

# Create image and drawing objects
img = Image.new('RGB', (400, 400), (255, 255, 255))
draw = ImageDraw.Draw(img)

# Calculate the end point of the line
x = 200 + 100 * math.cos(math.radians(angle))
y = 200 + 100 * math.sin(math.radians(angle))

# Draw the line on the image
draw.line((200, 200, x, y), fill=(0, 0, 0), width=3)

# Export the image as a .png file
filename = "angle_" + str(angle) + ".png"
img.save(filename, "PNG")
