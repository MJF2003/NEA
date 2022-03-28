from PIL import Image
from pathlib import Path

path = Path("../src/testImages")
name = "1st6.jpg"

file_loc = path / name

im = Image.open(file_loc)
im.save(path / f"{name.split('.')[0]}.bmp")
