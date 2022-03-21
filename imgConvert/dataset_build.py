import PIL.Image
import os
import numpy as np
from pathlib import Path

from main import full_edges

dir_path = Path("../data")


for subdir in os.listdir(dir_path / "classified"):
    for filename in os.listdir(dir_path / "classified" / subdir):
        egs = full_edges(f"{dir_path / 'classified' / subdir / filename}")
        imarray = np.array(egs.data)
        im = PIL.Image.fromarray(imarray)
        im = im.convert("L")
        im.save(f"{dir_path / 'raw_egs' / filename}")
