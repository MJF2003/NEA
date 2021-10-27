from class0 import *


def main():
    testimg = Image("../testImages/test.bmp")
    testimg.file.header.print_header()
    testimg.array_pixels()



if __name__ == "__main__":
    main()
