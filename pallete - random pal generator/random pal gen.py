import random

num_palettes = int(input("How many palettes would you like to generate? "))

for i in range(num_palettes):
    # Open file for writing
    filename = f"palette_{i+1}.pal"
    with open(filename, "w") as f:
        # Write JASC-PAL header
        f.write("JASC-PAL\n0100\n256\n")
        
        # Generate 256 randomized color values
        for j in range(256):
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            f.write(f"{red} {green} {blue}\n")
    
    print(f"Generated {filename}")