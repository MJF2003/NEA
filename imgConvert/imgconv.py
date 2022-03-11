from PIL import Image


path = "C:\\Users\\Michael Fahey\\PycharmProjects\\NEA\\testImages"
name = "ageas-roadsigns-.png"

im = Image.open(f"{path}\\{name}")
im.save(f"../testImages/{name}.bmp")

