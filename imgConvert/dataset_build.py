import PIL.Image
import os
from pathlib import Path



dir_path = Path("../dataset")


for idx, filename in enumerate(os.listdir(dir_path)):
    im = PIL.Image.open(dir_path / filename)
    im = im.resize((350, 350))
    loc = f"../data/raw/{idx}.bmp"
    im.save(loc)


