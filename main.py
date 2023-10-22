import string
import random
from PIL import Image, ImageDraw, ImageFont
from rich.console import Console

def generate_random_chars(length: int):
    "Function to generate random chars"
    
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def generate_ascii_gif(text: str, output_file: str = "ascii_art.gif", width: int = 600, height: int = 600) -> None:
    """
    Function to generate ascii art.
    
    :param text: The displayed text
    :param output_file: Location of the generated file
    :param width: The width of the gif
    :param height: The height of the gif
    """

    frames = []
    for i in range(100):
        img = Image.new("RGB", (width, height), "black")
        draw = ImageDraw.Draw(img)
    
        surrounding_text = generate_random_chars(width * height)
    
        font = ImageFont.truetype("Courier New.ttf", 10)
        font_big = ImageFont.truetype("Courier New.ttf", 40)
    
        x, y = 0, 0
        for char in surrounding_text:
            draw.text((x, y), char, fill="white", font=font)
            x += 10
            if x >= width:
                x = 0
                y += 10
    
        frames.append(img)

    text_x = (width - len(text) * 40) / 2 + 30
    text_y = (height - 40) / 2
    draw.text((text_x, text_y), text, fill="white", font=font_big)
    
    frames[0].save(
        output_file,
        save_all=True,
        append_images=frames[1:],
        duration=100,
        loop=0,
    )

if __name__ == "__main__":
    text = input("Enter the text of the ascii gif: ")

    console = Console()

    with console.status("[green]Generating Gif... (This may take a few minutes)"):
        generate_ascii_gif(text)

    print("Saved Gif to ascii_art.gif")
      
