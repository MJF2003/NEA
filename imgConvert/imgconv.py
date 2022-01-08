from PIL import Image


path = "C:\\Users\\Michael Fahey\\Downloads\\"
name = "bendir"

im = Image.open(f"{path}\\{name}.jpg")
im.save(f"../testImages/{name}.bmp")

