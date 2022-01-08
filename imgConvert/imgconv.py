from PIL import Image


path = "C:\\Users\\Michael Fahey\\Downloads\\"
name = "bendir.jpg"

im = Image.open(f"{path}\\{name}")
im.save(f"../testImages/{name}.bmp")

