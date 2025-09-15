# main.py
from imageGen.imageGen import simple_generate_image
from ASCIIgen.ASCIIgen import convert_to_ascii  

# -------------------- 1. Generate Image --------------------
image_path = simple_generate_image(
    "A cute golden retriever puppy playing in a sunny park, highly detailed, realistic style",
    "images/dog.png"  # Make sure 'images/' folder exists
)
print(f"Image saved at: {image_path}")

# -------------------- 2. Convert Image to ASCII --------------------
ascii_output_path = "ascii_art/dog_ascii.txt"  # ASCII art saved here
ascii_art = convert_to_ascii(image_path, output_file=ascii_output_path, width=120)

print("\n------ ASCII ART ------\n")
print(ascii_art)
print(f"\nASCII art saved at: {ascii_output_path}")
