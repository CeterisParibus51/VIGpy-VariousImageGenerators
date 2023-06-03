import re

# Load ASCII dictionary from file
ascii_dict = {}
with open("ascii_dict.txt", "r") as f:
    for line in f:
        match = re.match(r"'(.)': \((\d+),\s*(\d+),\s*(\d+)\)", line.strip())
        if match:
            ascii_char, r, g, b = match.groups()
            ascii_dict[ascii_char] = (int(r), int(g), int(b))
        else:
            print(f"Invalid input line: {line}")

# Load input text from file
input_text = []
with open("input.txt", "r") as f:
    for line in f:
        input_text.append(line.strip())

# Get dimensions of input text
num_lines = len(input_text)
num_cols = max(len(line) for line in input_text)

# Convert input text to RGB values
output_rgb = []
for y, line in enumerate(input_text):
    for x, char in enumerate(line):
        if char in ascii_dict:
            output_rgb.append((x, y, *ascii_dict[char]))

# Save output to file
with open("output.txt", "w") as f:
    f.write(f"Total X : {num_cols}\n")
    f.write(f"Total Y : {num_lines}\n")
    for rgb in output_rgb:
        f.write(f"({rgb[0]},{rgb[1]}) ({rgb[2]},{rgb[3]},{rgb[4]})\n")
