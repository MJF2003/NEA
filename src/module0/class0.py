# # # # # # # # # # # # # # # General Function Definitions # # # # # # # # # # # # # # #
from src import Arr2d


def little_endian(array_slice):
    # Return a hex string given a little endian slice by reversing the slice and filling it to 2 nibbles
    return "".join([str(j[2:].zfill(2)) for j in array_slice[::-1]])


def indivgs(pixel: list):  # Decimalises and returns a weighted greyscale pixel value based on RGB channels
    rgb, norm = [0.2989, 0.5870, 0.1140], 255
    return sum([int(channel, 16) * (rgb[idx] / norm) for idx, channel in enumerate(pixel[::-1])])


def lstsplit(array, split: int):  # Split a list at a given interval
    return [array[index:index + split] for index in range(0, len(array), split)]


# # # # # # # # # # # # End of General Function Definitions # # # # # # # # # # # # # #
# # # # # # # # # File Definition Nonsense # # # # # # # # # #


class Header:  # Header object created by file at file import containing all relevant file details
    def __init__(self):
        self.type = "UNSET"  # Should be set to BM
        self.size = -1  # An integer in bytes
        self.offset = -1  # An integer in bytes
        self.hsize = -1  # An integer in bytes equal to 40
        self.width = -1  # An integer in pixels
        self.height = -1  # An integer in pixels
        self.depth = -1  # Colour Depth in bits per pixel - should be 24
        self.swidth = -1  # Split width for arraying
        self.sheight = -1  # Split height for arraying

    def print_header(self):  # Predominantly for testing
        attrdict = {
            "File Type": self.type,
            "File Size": self.size,
            "Pixel Offset": self.offset,
            "Header Size": self.hsize,
            "Image Width": self.width,
            "Image Height": self.height,
            "Colour Depth": self.depth,
            "Split Height": self.sheight,
            "Split Width": self.swidth
        }
        for key, value in attrdict.items():
            print(f"{key:<20}: {value:<10}")

    def reset(self):
        self.__init__()


class File:  # Object which contains both image and header data. Reception class for incoming image
    def __init__(self, filename):
        self.filename = filename
        self.header = None
        with open(self.filename, "rb") as file:
            self.data = [hex(byte) for byte in file.read()]  # Reads pixel stream as hex vals into 1D array

    def create_header(self):  # Infers values of  each header attribute from .bmp file protocol defined intervals
        self.header = Header()
        self.header.type = "".join([chr(int(i, 16)) for i in self.data[0:2]])
        self.header.size = int(little_endian(self.data[2:6]), 16)
        self.header.offset = int(little_endian(self.data[10:14]), 16)
        self.header.hsize = int(little_endian(self.data[14:18]), 16)
        self.header.width = int(little_endian(self.data[18:22]), 16)
        self.header.height = int(little_endian(self.data[22:26]), 16)
        self.header.depth = int(little_endian(self.data[28:30]), 16)
        self.header.swidth = int(self.header.width * (self.header.depth / 8))  # Split width
        self.header.sheight = int(self.header.height * (self.header.depth / 8))  # Split height


# # # # # # # # # End of File Nonsense # # # # # # # # # #


class Image(Arr2d):
    def __init__(self, filename):
        self.filename = filename
        self.file = File(self.filename)
        self.file.create_header()
        super().__init__(self.file.header.width, self.file.header.height)
        self.pixelsraw = self.file.data[self.file.header.offset:]
        xpadding = (4 - self.file.header.swidth % 4) % 4  # This gets DWORD padding
        rows = lstsplit(self.pixelsraw, self.file.header.swidth + xpadding)[::-1]
        rgbpxls = list(map(lambda row: lstsplit(row[:len(row) - xpadding], int(self.file.header.depth / 8)), rows))
        self.data = [list(map(indivgs, row)) for row in rgbpxls]
