from PIL import Image
import os

# -------------------- ENHANCED ASCII CHARACTERS --------------------
# Smooth gradient: darker pixels -> denser characters
ASCII_CHARS = ["@", "%", "#", "*", "+", "=", "-", ":", ".", " "]

# -------------------- HELPER FUNCTIONS --------------------

def resize_image(image: Image.Image, new_width: int = 50) -> Image.Image:
    """
    Resize image while maintaining aspect ratio.
    Smaller width and adjusted height give better proportions for ASCII.
    """
    width, height = image.size
    ratio = height / width
    new_height = max(1, int(new_width * ratio * 0.5))  # adjust for ASCII character ratio
    return image.resize((new_width, new_height))

def grayify(image: Image.Image) -> Image.Image:
    """Convert image to grayscale (black & white)."""
    return image.convert("L")

def pixels_to_ascii(image: Image.Image) -> str:
    """
    Map each pixel to an ASCII character based on brightness.
    More levels = smoother shading.
    """
    pixels = image.getdata()
    return "".join(
        ASCII_CHARS[min(len(ASCII_CHARS)-1, pixel * len(ASCII_CHARS) // 256)]
        for pixel in pixels
    )

def convert_to_ascii(image_path: str, output_file: str = None, width: int = 50) -> str:
    """
    Convert an image to high-quality ASCII art.
    
    :param image_path: Path to input image
    :param output_file: Optional path to save ASCII art as a text file
    :param width: Width of ASCII art in characters (smaller = more compact)
    :return: ASCII art as a string
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image '{image_path}' does not exist.")

    image = Image.open(image_path)
    image = resize_image(image, width)
    image = grayify(image)

    ascii_str = pixels_to_ascii(image)
    ascii_lines = [ascii_str[i:i+width] for i in range(0, len(ascii_str), width)]
    ascii_art = "\n".join(ascii_lines)

    if output_file:
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(ascii_art)

    return ascii_art
