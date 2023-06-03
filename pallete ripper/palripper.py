import os
import PIL
from PIL import Image

# Define input and output folders
input_folder = 'rip'
output_folder = 'pal'

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all images in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg'):
        filepath = os.path.join(input_folder, filename)
        # Open the image
        with Image.open(filepath) as img:
            # Extract the palette
            palette = img.getpalette()
            # Create a new palette file in JASC format
            pal_filename = os.path.splitext(filename)[0] + '.pal'
            pal_filepath = os.path.join(output_folder, pal_filename)
            with open(pal_filepath, 'w') as f:
                f.write('JASC-PAL\n0100\n256\n')
                for i in range(256):
                    rgb = palette[i*3:i*3+3]
                    f.write(f'{rgb[0]} {rgb[1]} {rgb[2]}\n')