from module0 import class0
from math import pi, exp


def gauss_func(x, y, sigma):
    return 1 / (2 * pi * (sigma ** 2)) * exp(-((x ** 2 + y ** 2) / (2 * (sigma ** 2))))


def convolve(array, altmat: list):
    acc = 0
    for y, row in enumerate(array):
        for x, col in enumerate(row):
            acc += col * altmat[y][x]
    return acc


def gaussian_kernel(size, sigma=1.2):
    mid = (size + 1) / 2
    kernel = [[gauss_func((x + 1) - mid, (y + 1) - mid, sigma) for x in range(size)] for y in range(size)]
    return kernel


class SymMat(class0.Arr2d):
    def __init__(self, size):
        super().__init__(size, size)
        self.zeros()
        self.mid = (size - (size % 2)) / 2, (size - (size % 2)) / 2




class Gsimg(class0.Arr2d):
    def __init__(self, image_object: class0.Image, width, height):
        super().__init__(width, height)
        self.pxls = image_object.data
        self.data = [[px[0] for px in row] for row in self.pxls]



