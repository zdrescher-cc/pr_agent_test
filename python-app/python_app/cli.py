import click
from PIL import Image
import numpy as np


@click.group()
def cli():
    """Command line utility for python-app."""
    pass


@cli.command()
@click.option("--name", default="World", help="Who to greet")
def hello(name):
    """Simple command that greets the user."""
    click.echo(f"Hello, {name}!")


@cli.command()
@click.argument('image_path', type=click.Path(exists=True))
@click.option('--width', default=100, help='Width of the output ASCII art')
@click.option('--output', '-o', help='Output file path (optional)')
def image2ascii(image_path, width, output):
    """Convert an image to ASCII art."""
    # ASCII chars to represent different pixel intensities
    ASCII_CHARS = "@%#*+=-:. "

    # Open and convert image to grayscale
    image = Image.open(image_path).convert('L')
    
    # Calculate new dimensions maintaining aspect ratio
    aspect_ratio = image.height / image.width
    height = int(width * aspect_ratio * 0.5)  # * 0.5 to account for terminal char spacing
    image = image.resize((width, height))
    
    # Convert image to numpy array
    pixels = np.array(image)
    
    # Convert pixels to ASCII characters
    ascii_str = ''
    for row in pixels:
        for pixel in row:
            index = int((pixel / 255) * (len(ASCII_CHARS) - 1))
            ascii_str += ASCII_CHARS[index]
        ascii_str += '\n'
    
    if output:
        # Save to file if output path is provided
        with open(output, 'w') as f:
            f.write(ascii_str)
        click.echo(f"ASCII art saved to {output}")
    else:
        # Print to console
        click.echo(ascii_str)


if __name__ == "__main__":
    cli()
