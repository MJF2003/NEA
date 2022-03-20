from PIL import Image
from pathlib import Path

path = Path("../testImages")
name = "myNSL.jpg"

file_loc = path / name

im = Image.open(file_loc)
im = im.resize((350, 350))
im.save(f"../testImages/{name.split('.')[0]}.bmp")
