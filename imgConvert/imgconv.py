from PIL import Image
from pathlib import Path

path = Path("../testImages")
name = "30mph.jfif"

file_loc = path / name

im = Image.open(file_loc)
im.save(f"../testImages/{name.split('.')[0]}.bmp")
