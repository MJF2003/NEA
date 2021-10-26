def little_endian(array_slice):
    return "".join([str(j[2:].zfill(2)) for j in array_slice[::-1]])


class Header:
    def __init__(self):
        self.type = "UNSET"     # Should be set to BM
        self.size = -1          # An integer in bytes
        self.offset = -1        # An integer in bytes
        self.hsize = -1         # An integer in bytes equal to 40
        self.width = -1         # An integer in pixels
        self.height = -1        # An integer in pixels
        self.depth = -1         # Colour Depth in bits per pixel - most likely 24

    def print_header(self):
        pass


class File:
    def __init__(self, filename):
        self.filename = filename
        self.header = None
        pass


    def create_header(self):
        self.header = Header()
        with open(self.filename, "rb") as file:
            data = [hex(byte) for byte in file.read()]
        self.header.type = "".join([chr(int(i, 16)) for i in data[0:2]])
        self.header.size = int(little_endian(data[2:6]), 16)
        self.header.offset = int(little_endian(data[10:14]), 16)
        self.header.hsize = int(little_endian(data[14:18]), 16)
        self.header.width = int(little_endian(data[18:22]), 16)
        self.header.height = int(little_endian(data[22:26]), 16)
        self.header.depth = int(little_endian(data[28:30]), 16)


    def print_data(self):
        with open(self.filename, "rb") as file:
            data = [byte for byte in file.read()[54:]]
            print(data)


    def print_hex(self):
        self.header.print_header()
        print("#####  End of header  #####")
        self.print_data()


    def print_raw(self):
        with open(self.filename, "rb") as file:
            buffer = [hex(i) for i in file.read()]
            print(buffer[:100])
