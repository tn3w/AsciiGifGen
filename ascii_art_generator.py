import string
import random
from PIL import Image, ImageDraw, ImageFont
from rich.progress import Progress
from time import time

CHARS = string.ascii_letters + string.digits

def generate_random_chars(length: int):
    "Function to generate random chars"

    return ''.join(random.choice(CHARS) for _ in range(length))

def generate_ascii_gif(text: str, output_file: str = "ascii_art.gif", width: int = 600, height: int = 200, quite: bool = False) -> None:
    """
    Function to generate ascii art.
    
    :param text: The displayed text
    :param output_file: Location of the generated file
    :param width: The width of the gif
    :param height: The height of the gif
    :param quite: If True, No Console Output
    """

    frames = []

    font = ImageFont.truetype("Courier New.ttf", 10)
    font_big = ImageFont.truetype("Courier New.ttf", 40)

    text_x = (width - len(text) * 40) / 2 + 30
    text_y = (height - 40) / 2

    progress = Progress()

    with progress:
        if not quite:
            task = progress.add_task(f"[cyan]Generating GIF Frames...", total=13)
        for i in range(12):
            img = Image.new("RGB", (width, height), "black")
            draw = ImageDraw.Draw(img)

            surrounding_text = generate_random_chars(width * height)

            draw.text((text_x, text_y), text, fill="white", font=font_big)
        
            x, y = 0, 0
            for char in surrounding_text:
                draw.text((x, y), char, fill="white", font=font)
                x += 10
                if x >= width:
                    x = 0
                    y += 10
        
            frames.append(img)

            if not quite:
                progress.update(task, completed=i+1)
    
    frames[0].save(
        output_file,
        save_all=True,
        append_images=frames[1:],
        duration=10,
        loop=0,
    )

if __name__ == "__main__":
    text = input("Enter the text of the ascii gif: ")
    
    start_time = time()
    generate_ascii_gif(text)
    end_time = time()

    print("Saved Gif to ascii_art.gif (took", (end_time-start_time) / 60, "m)")
      
