from func import *
from math import pi, exp, atan



def gauss(x, y, sigma):  # Calculate gaussian value, given position in the gaussian matrix measured from the centre
    return 1 / (2 * pi * (sigma ** 2)) * exp(-((x ** 2 + y ** 2) / (2 * (sigma ** 2))))


def gaussian_kernel(size, sigma=1):  # Assemble a gaussian kernel matrix of a defined size and standard deviation
    kn = SymMat(size)
    kn.data = [[gauss(x - kn.mid, y - kn.mid, sigma) for x in range(kn.width)] for y in range(kn.height)]
    return kn


def sobelx():  # Defines the Sobel X filter as a symmetrical matrix class
    kn = SymMat(3)
    kn.data = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    return kn


def sobely():  # Defines the Sobel Y filter as a symmetrical matrix class
    kn = SymMat(3)
    kn.data = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    return kn


def surround(data, x, y):
    srnd = SymMat(3)  # Defines the immediately adjacent pixels to the pixel in question
    srnd.data = [[data[y - 1][x - 1], data[y - 1][x], data[y - 1][x + 1]],
                 [data[y][x - 1], data[y][x], data[y][x + 1]],
                 [data[y + 1][x - 1], data[y + 1][x], data[y + 1][x + 1]]]
    return srnd


def nms(angle, srnd):  # Perfoms checking on the relevant adjacent pixels given the angle and a 3x3 of pixels
    to_check = [
        ((2, 1), (0, 1)),  # If angle is 0 rad
        ((0, 0), (2, 2)),  # If angle is pi/4 rad
        ((1, 0), (1, 2)),  # If angle is pi/2 rad
        ((2, 0), (0, 2))   # If angle is -pi/4
    ]
    idx = int(angle/(pi/4))  # Calculates index of to_check list
    if srnd.data[1][1] < srnd.xy(*to_check[idx][0]) or srnd.data[1][1] < srnd.xy(*to_check[idx][1]):
        return False  # Returns false if there is a greater intensity in either relevant adj pixel
    return True  # Returns true if the current pixel is the maximum


class Edges(Arr2d):
    def __init__(self, image):
        super().__init__(image.width, image.height)
        self.xedges = Arr2d(image.width, image.height)
        self.xedges.data = convolve(image, sobelx())
        self.yedges = Arr2d(image.width, image.height)
        self.yedges.data = convolve(image, sobely())
        self.data, self.angles = self.compound()
        self.strongval = 1
        self.weakval = 0.4
        self.irrval = 0


    def compound(self):
        magn = Arr2d(self.width, self.height)  # Assesses the magnitude of each pixel in the edge array
        angs = Arr2d(self.width, self.height)  # Assesses the angle of each edge to the nearest pi/4 window
        for y in range(self.height):
            for x in range(self.width):  # Iterate through each pixel
                magn.data[y][x] = (self.xedges.data[y][x]**2 + self.yedges.data[y][x]**2)**0.5
                # Calculate magnitude using sqrt(x**2 + y**2)
                try:
                    angs.data[y][x] = round(atan(self.yedges.data[y][x] / self.xedges.data[y][x]) / (pi/4))*(pi/4)
                except ZeroDivisionError:
                    angs.data[y][x] = pi/2  # Takes into account the inability to find an tan value for pi/2
                # Calculate angle of the edge measured from the horizontal
        return magn.data, angs.data

    def nonmax(self):  # Runs NMS on each pixel in the edge array
        for y in range(1, self.height - 1):
            for x in range(1, self.width - 1):
                srnd = surround(self.data, x, y)
                if not nms(self.angles[y][x], srnd):  # Checks if it is the maximum pixel
                    self.data[y][x] = 0  # Sets to zero if not

    def dblthresh(self, low, high):  # Runs double thresholding on each pixel
        for y in range(1, self.height - 1):
            for x in range(1, self.width - 1):
                px = self.data[y][x]
                if px > high:
                    self.data[y][x] = self.strongval  # High value (strong) pixels are set to white
                elif px > low:
                    self.data[y][x] = self.weakval  # Mid value (weak) pixels are set to grey
                else:
                    self.data[y][x] = self.irrval  # Low value (irrelevant) pixels are set to black
                    
    def hysteresis(self):  # Runs hysteresis tracking on each pixel
        for y in range(1, self.height - 1):
            for x in range(1, self.width - 1):
                px = self.data[y][x]
                if px == self.weakval:  # Checks if pixel is weak
                    srnd = surround(self.data, x, y).flatten()
                    if 1 in srnd:  # If strong pixel in surroundings then mark current pixel as strong
                        self.data[y][x] = self.strongval
                    else:
                        self.data[y][x] = self.irrval

    def invert(self):
        for y in range(self.height):
            for x in range(self.width):
                self.data[y][x] = 1 - self.data[y][x]


class SymMat(Arr2d):
    def __init__(self, size):
        super().__init__(size, size)
        self.mid = (size - (size % 2)) / 2  # Allows int mid value for both odd and even sizes
