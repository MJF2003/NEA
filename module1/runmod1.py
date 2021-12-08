from module1.class1 import *
from module0.class0 import *


def main():
    testimg = Image("../testImages/sdjm.bmp")
    testimg.display()
    testimg.asciiart()
    # for y, row in enumerate(procimg.data[2:-2], 2):
    #     for x, px in enumerate(row[2:-2], 2):
    #         matx = [[px for px in row[x - 2:x + 2]] for row in procimg.data[y - 2:y + 2]]
    #         procimg.data[y][x] = convolve(matx, gaussian_kernel(5))
    # procimg.display()





if __name__ == "__main__":
    main()

