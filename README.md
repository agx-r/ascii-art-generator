# ASCII Art Generator

The ASCII Art Generator is a Python module that allows you to convert images into ASCII art. It provides a simple and customizable way to transform images into text-based representations, suitable for various creative and visual purposes.

## Features

- Resize images while maintaining their aspect ratio.
- Convert images to grayscale for better representation.
- Generate ASCII art using a default or custom set of ASCII characters.
- Option to save the generated ASCII art to a text file.
- Command-line interface for easy usage.

## Installation

1. Make sure you have Python 3.x installed on your system.
2. Clone or download this repository to your local machine.
3. Open a terminal and navigate to the project directory.
4. Install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Usage

The ASCII Art Generator can be used both as a standalone script and as a Python module. Here are some examples of how to use it:

### Command-Line Interface

To generate ASCII art from an image using the command line, navigate to the project directory and use the following command:

```bash
python ascii_art_generator.py input_image_path [--output_width OUTPUT_WIDTH] [--ascii_chars ASCII_CHARS] [--output_file OUTPUT_FILE]
```

- `input_image_path`: Path to the input image.
- `--output_width`: Width of the output ASCII art (default is 64).
- `--ascii_chars`: Custom ASCII characters for the art (default is predefined set).
- `--output_file`: Path to save the ASCII art as a text file.

Example:

```bash
python ascii_art_generator.py input.jpg --output_width 80 --ascii_chars "@#* ."
```

### Python Module

You can also use the ASCII Art Generator as a Python module within your own scripts:

```python
from ascii_art_generator import load_image, generate_ascii_art, save_ascii_art_to_file

input_image = load_image("input.jpg")
ascii_art = generate_ascii_art(input_image, output_width=80, ascii_chars="@#* .")
save_ascii_art_to_file(ascii_art, "output.txt")
```

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

The ASCII Art Generator module uses the following third-party libraries:

- [PIL (Pillow)](https://pillow.readthedocs.io/en/stable/): Python Imaging Library for image manipulation.
- [NumPy](https://numpy.org/): Scientific computing library for numerical operations.

## Feedback and Contributions

If you have any feedback, suggestions, or would like to contribute to this project, feel free to [open an issue](https://github.com/agx-r/ascii-art-generator/issues) or [submit a pull request](https://github.com/agx-r/ascii-art-generator/pulls). Your contributions are highly appreciated!

Enjoy creating fascinating ASCII art with the ASCII Art Generator module!
