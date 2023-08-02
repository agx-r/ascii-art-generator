import numpy as np
from PIL import Image

# Constants
DEFAULT_ASCII_CHARS = '@%#*+=-:. '

def resize_image(image, new_width=100):
    """Resize the image while maintaining aspect ratio."""
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    return image.resize((new_width, new_height))

def grayscale_image(image):
    """Convert the image to grayscale."""
    return image.convert('L')

def image_to_ascii(image, output_width=100, ascii_chars=DEFAULT_ASCII_CHARS):
    """Convert the image to ASCII art."""
    image = resize_image(image, output_width)
    image = grayscale_image(image)
    pixels = np.array(image)

    pixel_range = len(ascii_chars) - 1
    ascii_str = '\n'.join(
        ''.join(ascii_chars[pixel_value * pixel_range // 255] for pixel_value in row)
        for row in pixels
    )

    return ascii_str

def generate_ascii_art(input_image_path, output_width=100, ascii_chars=DEFAULT_ASCII_CHARS):
    """Generate ASCII art from an image file."""
    try:
        image = Image.open(input_image_path)
    except FileNotFoundError:
        return "Error: The specified image file was not found."
    except Exception as e:
        return f"Error: {e}"

    ascii_art = image_to_ascii(image, output_width, ascii_chars)
    return ascii_art

if __name__ == '__main__':
    input_image_path = 'input_image.jpg'
    output_width = 64
    ascii_art = generate_ascii_art(input_image_path, output_width)
    print(ascii_art)
