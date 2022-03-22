import PIL.Image
import os
import numpy as np
from pathlib import Path

from main import full_edges

dir_path = Path("data")


for subdir in os.listdir(dir_path / "classified"):
    for filename in os.listdir(dir_path / "classified" / subdir):
        egs = full_edges(f"{dir_path / 'classified' / subdir / filename}")
        egs.display(f"{filename}")
        imarray = np.array(egs.data)
        im = PIL.Image.fromarray((imarray * 255).astype('uint8'), mode='L')
        im.save(f"{dir_path / 'raw_egs' / subdir / filename.split('.')[0]}.png")
