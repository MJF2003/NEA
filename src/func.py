import copy
from datetime import datetime as dt
from matplotlib.pyplot import imshow, show, title
from pathlib import Path


# General Purpose validity checker
def valid(vtype: str, ipt, comp=None) -> bool:
    """
    General purpose validation tool for input sanitisation
    :param vtype: Validation Type - Selected from 'EQ'(Equal to), 'GT'(Greater than)', 'LT'(Less than),
    'BT'(Between), 'DG'(Digit)
    :param ipt: Input string to check
    :param comp: Comparison - either missing, a single value or a tuple of top and bottom limits
    :return: True or False dependent on meeting conditions
    """
    try:
        if vtype == "EQ":
            return ipt == comp
        elif vtype == "GT":
            return ipt > comp
        elif vtype == "LT":
            return ipt < comp
        elif vtype == "BT":
            return comp[0] < int(ipt) < comp[1]
        elif vtype == "DG":
            return ipt.isdigit()
        else:
            return True
    except:
        return False


def get_path(path_from_root):  # Any system file path handler
    """
    Uses environment variables to ensure a complete path to the desired file.
    :param path_from_root: A file path directed from the NEA root project folder
    :return: Python Path Object relevant to OS
    """
    root = Path(__file__).parent.parent
    file_path = root / Path(path_from_root)
    return file_path


# # # # # # # # # # # # General 2D Array Class Definition # # # # # # # # # # # #
def convolve(data, kn):
    """
    Matrix convolution function.
    Find Kernel TL * Sub-Mat TL + Kernel TM * Sub-Mat TM + Kernel TR * Sub-Mat TR +
    Kernel ML * Sub-Mat ML + Kernel MM * Sub-Mat MM + Kernel MR * Sub-Mat MR +
    Kernel BL * Sub-Mat BL + Kernel BM * Sub-Mat BM + Kernel BR * Sub-Mat BR
    for 3x3 Kernel. But will work for any size kernel. Applies to every Sub-Matrix in the image
    :param data: Large 2D array of values
    :param kn: Small, symmetrical 2D array
    :return: Output 2D array of same size as data
    """
    ckn = copy.deepcopy(kn)
    pad = int(ckn.mid)
    output = [list(row) for row in data]
    for row_no in range(pad, len(data)-pad):
        for pxl_no in range(pad, len(data[row_no])-pad):
            px = [kn.data[y][x] * data[row_no + y - pad][pxl_no + x - pad] for y in range(ckn.height) for x in range(ckn.width)]
            output[row_no][pxl_no] = sum(px)
    return output


class Arr2d:  # General 2D Array Class with common methods
    """
    General 2D Array Class describing common methods which applie to 2D arrays in the context of image processing
    """
    def __init__(self, width, height):
        """
        Initialises an array of the correct size upon instantiation.
        This is because changing an array value is faster than appending.
        :param width: Width of the 2D array
        :param height: Height of the 2D array
        """
        self.width = width
        self.height = height
        self.data = []
        self.zeros()  # Initalise full of zeros


    def zeros(self):
        """
        Uses List Comprehension to fill the data with zeros
        """
        self.data = [[0 for a in range(self.width)] for b in range(self.height)]

    def xy(self, x, y):
        """
        Returns a value based on the x and y coordinates
        :param x: x (column) coordinate
        :param y: y (row) coordinate
        :return: Value stored at that coordinate
        """
        return self.data[y][x]

    def flatten(self):
        """
        Returns the data as 1D array - bins off rows
        :return: Single dimension array row by row sequentially from top to bottom
        """
        return [x for y in self.data for x in y]

    def getrow(self, y):
        """
        Returns a row given a y value
        :param y: Row coordinate
        :return: The row as a single dimension array
        """
        return self.data[y]

    def getcol(self, x):
        """
        Returns a column given an x value
        :param x: Column coordinate
        :return: The column as a single dimension array
        """
        return [self.data[y][x] for y in range(self.height)]

    def display(self, titlestr):
        """
        Uses MPL to plot the data as an image with greyscale colour mapping
        :param titlestr: The title to be displayed in the plot
        :return: None
        """
        imshow(self.data, cmap="gray")
        title(str(titlestr))
        show()

    def asciiart(self, file_loc):
        """
        Writes ASCII art of the image to a file
        :param file_loc: Save location for the output file
        :return: None
        """
        reps = ["$", "@", "B", "%", "8", "&", "W", "M", "#", "*", "o", "a", "h", "k", "b", "d", "p", "q", "w", "m",
                "Z", "O", "0", "Q", "L", "C", "J", "U", "Y", "X", "z", "c", "v", "u", "n", "x", "r", "j", "f", "t",
                "/", "\\", "|", "(", ")", "1", "{", "}", "[", "]", "?", "-", "_", "+", "~", "<", ">", "i", "!", "l",
                "I", ";", ":", "\"", "^", "`", "'", ".", " "]
        filename = Path(file_loc / f"{dt.now().year}-{dt.now().month}-{dt.now().day}-{str(dt.now().hour).zfill(2)}\
{str(dt.now().minute).zfill(2)}{str(dt.now().second).zfill(2)}.txt")
        with open(filename, "a") as f:
            for row in self.data:
                f.write("".join([reps[round(px * len(reps)) - 1] for px in row]))
                f.write("\n")


# # # # # # # # # # # # End of General 2D Array Class Definition # # # # # # # # # # # #
