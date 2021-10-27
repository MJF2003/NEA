
def little_endian(array_slice):                         # Return a hex string given a little endian slice
    return "".join([str(j[2:].zfill(2)) for j in array_slice[::-1]])


def ngreyscale(pixel: list) -> float:     # Return a value between 0 and 1 of greyscale intensity
    return sum([int(i, 16) for i in pixel]) / (255 * len(pixel))


def lstsplit(array, split: int):
    return [array[index:index + split] for index in range(0, len(array), split)]


class Header:
    def __init__(self):
        self.type = "UNSET"     # Should be set to BM
        self.size = -1          # An integer in bytes
        self.offset = -1        # An integer in bytes
        self.hsize = -1         # An integer in bytes equal to 40
        self.width = -1         # An integer in pixels
        self.height = -1        # An integer in pixels
        self.depth = -1         # Colour Depth in bits per pixel - should be 24
        self.swidth = -1        # Split width for arraying
        self.sheight = -1       # Split height for arraying


    def print_header(self):
        attrdict = {
            "File Type": self.type,
            "File Size": self.size,
            "Pixel Offset": self.offset,
            "Header Size": self.hsize,
            "Image Width": self.width,
            "Image Height": self.height,
            "Colour Depth": self.depth,
        }
        for key, value in attrdict.items():
            print(f"{key:<20}: {value:<10}")


class File:
    def __init__(self, filename):
        self.filename = filename
        self.header = None
        with open(self.filename, "rb") as file:
            self.data = [hex(byte) for byte in file.read()]


    def create_header(self):
        self.header = Header()
        self.header.type = "".join([chr(int(i, 16)) for i in self.data[0:2]])
        self.header.size = int(little_endian(self.data[2:6]), 16)
        self.header.offset = int(little_endian(self.data[10:14]), 16)
        self.header.hsize = int(little_endian(self.data[14:18]), 16)
        self.header.width = int(little_endian(self.data[18:22]), 16)
        self.header.height = int(little_endian(self.data[22:26]), 16)
        self.header.depth = int(little_endian(self.data[28:30]), 16)
        self.header.swidth = int(self.header.width * (self.header.depth / 8))       # Split width
        self.header.sheight = int(self.header.height * (self.header.depth / 8))     # Split height



class Image:
    def __init__(self, filename):
        self.file = File(filename)
        self.file.create_header()
        self.pixelsraw = self.file.data[self.file.header.offset:]
        self.pixels = []
        self.xpadding = 4 - int((self.file.header.width * (self.file.header.depth / 8)) % 4)  # This gets DWORD padding


    def array_pixels(self):
        rows = lstsplit(self.pixelsraw, int(self.file.header.swidth + self.xpadding))
        realrows = [lstsplit(row[:-1 * self.xpadding], int(self.file.header.depth / 8)) for row in rows]
        return realrows

