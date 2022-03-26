import PIL.Image
import os
import numpy as np
from pathlib import Path

from src.main import full_edges

dir_path = Path("src/data")


for subdir in os.listdir(dir_path / "classified"):
    for filename in os.listdir(dir_path / "classified" / subdir):
        egs = full_edges(f"{dir_path / 'classified' / subdir / filename}")
        egs.display(f"{filename}")
        imarray = np.array(egs.data)
        im = PIL.Image.fromarray((imarray * 255).astype('uint8'), mode='L')
        im.save(f"{dir_path / 'classified_edges' / subdir / filename.split('.')[0]}.png")
