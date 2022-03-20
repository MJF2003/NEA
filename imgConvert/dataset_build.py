import PIL.Image
import os
from pathlib import Path

from main import full_edges

dir_path = Path("../../dataset")


for idx, filename in enumerate(os.listdir(dir_path)):
    im = PIL.Image.open(dir_path / filename)
    im = im.resize((350, 350))
    loc = f"{dir_path / 'bmp' / str(idx)}.bmp"
    im.save(loc)


