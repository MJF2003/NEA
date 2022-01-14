from func import *
from math import pi, exp, atan


def gauss(x, y, sigma):
    return 1 / (2 * pi * (sigma ** 2)) * exp(-((x ** 2 + y ** 2) / (2 * (sigma ** 2))))


def gaussian_kernel(size, sigma=1):
    kn = SymMat(size)
    kn.data = [[gauss(x - kn.mid, y - kn.mid, sigma) for x in range(kn.width)] for y in range(kn.height)]
    return kn


def sobelx():
    kn = SymMat(3)
    kn.data = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    return kn


def sobely():
    kn = SymMat(3)
    kn.data = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    return kn


def nms(x, y):
    pass


class Edges(Arr2d):
    def __init__(self, image):
        super().__init__(image.width, image.height)
        self.xedges = Arr2d(image.width, image.height)
        self.xedges.data = convolve(image, sobelx())
        self.yedges = Arr2d(image.width, image.height)
        self.yedges.data = convolve(image, sobely())
        self.data, self.angles = self.comp()


    def comp(self):
        magn = Arr2d(self.width, self.height)
        angs = Arr2d(self.width, self.height)
        for y in range(self.height):
            for x in range(self.width):
                magn.data[y][x] = (self.xedges.data[y][x]**2 + self.yedges.data[y][x]**2)**0.5
                try:
                    angs.data[y][x] = round(atan(self.yedges.data[y][x] / self.xedges.data[y][x]) / (pi/4))*(pi/4)
                except ZeroDivisionError:
                    angs.data[y][x] = pi/2
        return magn.data, angs.data

    def nonmax(self):
        for y in range(self.height):
            for x in range(self.width):
                nms()




class SymMat(Arr2d):
    def __init__(self, size):
        super().__init__(size, size)
        self.mid = (size - (size % 2)) / 2  # Allows int mid value for both odd and even sizes
