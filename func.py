import copy
from datetime import datetime as dt
from matplotlib.pyplot import imshow, show



def valid(vtype: str, ipt, comp) -> bool:
    if vtype == "EQ":
        return ipt == comp
    elif vtype == "GT":
        return ipt > comp
    elif vtype == "LT":
        return ipt < comp
    elif vtype == "BT":
        return comp[0] < ipt < comp[1]
    elif vtype == "DG":
        return ipt.isdigit()
    else:
        return True


# # # # # # # # # # # # General 2D Array Class Definition # # # # # # # # # # # #


def convolve(image, kn):
    ckn = copy.deepcopy(kn)
    pad = int(ckn.mid)
    data = image.data
    output = [list(row) for row in data]
    for rn in range(pad, len(data)-pad):
        for pn in range(pad, len(data[rn])-pad):
            px = [kn.data[y][x] * data[rn + y - pad][pn + x - pad] for y in range(ckn.height) for x in range(ckn.width)]
            output[rn][pn] = sum(px)
    return output


class Arr2d:  # General 2D Array Class with common methods
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = []
        self.zeros()  # Initalise full of zeros


    def zeros(self):  # Uses List Comprehension to fill the data with zeros
        self.data = [[0 for a in range(self.width)] for b in range(self.height)]

    def xy(self, x, y):  # Returns a value based on the x and y coordinates
        return self.data[y][x]

    def flatten(self):  # Returns the data as 1D array - bins off rows
        return [x for y in self.data for x in y]

    def getrow(self, y):  # Returns a row given a y value
        return self.data[y]

    def getcol(self, x):  # Returns a column given an x value
        return [self.data[y][x] for y in range(self.height)]

    def display(self):  # Uses MPL to plot the data as an image with greyscal colour mapping
        imshow(self.data, cmap="gray")
        show()

    def asciiart(self):
        reps = ["$", "@", "B", "%", "8", "&", "W", "M", "#", "*", "o", "a", "h", "k", "b", "d", "p", "q", "w", "m",
                "Z",
                "O", "0", "Q", "L", "C", "J", "U", "Y", "X", "z", "c", "v", "u", "n", "x", "r", "j", "f", "t", "/",
                "\\", "|", "(", ")", "1", "{", "}", "[", "]", "?", "-", "_", "+", "~", "<", ">", "i", "!", "l", "I",
                ";", ":", "\"", "^", "`", "'", ".", " "]
        filename = f"{dt.now().year}-{dt.now().month}-{dt.now().day}-{str(dt.now().hour).zfill(2)}\
{str(dt.now().minute).zfill(2)}{str(dt.now().second).zfill(2)}.txt"
        with open(filename, "a") as f:
            for row in self.data:
                f.write("".join([reps[round(px * len(reps)) - 1] for px in row]))
                f.write("\n")


# # # # # # # # # # # # End of General 2D Array Class Definition # # # # # # # # # # # #


class Program:
    def __init__(self):
        self.fileloaded = False
        self.status = "Initialising..."
        self.option = -1
        self.menu()

    def error(self, message: str, level):  # Error Display Program
        print(message)
        if level == 3:
            self.status = "Level 3 Error..."
            self.__init__()
        elif level == 2:
            self.status = "Level 2 Error..."
        elif level == 1:
            self.status = "Level 1 Error..."
        else:
            self.status = "Unknown Error"
        print(self.status)

    def menu(self):
        menu = {
            "1": ("Load File", self.loadfile(self.getpath())),
            "2": ("Plot File", self.plotfile()),
            "3": ("Edge Detect", self.edgedetect())
        }

        for key, value in menu.items():
            print(f"{key:<5}: {value[0]:<20}")

        option = input("Enter a number from the list above: ")
        while not valid("DG", option):
            option = input("Enter a number from the list above: ")
        print(self.status)

    def getpath(self):
        pass

    def loadfile(self, path):
        pass

    def plotfile(self):
        pass

    def edgedetect(self):
        pass

