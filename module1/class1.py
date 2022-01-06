from func import *
from math import pi, exp


def gauss(x, y, sigma):
    return 1 / (2 * pi * (sigma ** 2)) * exp(-((x ** 2 + y ** 2) / (2 * (sigma ** 2))))


def gaussian_kernel(size, sigma=1):
    kn = SymMat(size)
    kn.data = [[gauss(x - kn.mid, y - kn.mid, sigma) for x in range(kn.width)] for y in range(kn.height)]
    return kn


class SymMat(Arr2d):
    def __init__(self, size):
        super().__init__(size, size)
        self.mid = (size - (size % 2)) / 2  # Allows int mid value for both odd and even sizes
