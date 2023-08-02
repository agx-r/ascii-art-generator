import numpy as np
from PIL import Image

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    return image.resize((new_width, new_height))

def grayscale_image(image):
    return image.convert('L')

def image_to_ascii(image, width=100, ascii_chars='@%#*+=-:. '):
    image = resize_image(image, width)
    image = grayscale_image(image)
    pixels = np.array(image)

    pixel_range = len(ascii_chars) - 1
    ascii_str = '\n'.join(
        ''.join(ascii_chars[pixel_value * pixel_range // 255] for pixel_value in row)
        for row in pixels
    )

    return ascii_str

def generate_ascii_art(image_path, output_width, ascii_chars='@%#*+=-:. '):
    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        print("Error: The specified image file was not found.")
        return
    except Exception as e:
        print("Error:", e)
        return

    ascii_art = image_to_ascii(image, output_width, ascii_chars)
    return ascii_art

if __name__ == '__main__':
    input_image = 'input_image.jpg'
    width = 64
    ascii_art = generate_ascii_art(input_image, width)
    print(ascii_art)
