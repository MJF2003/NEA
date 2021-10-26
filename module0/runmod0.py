from class0 import File, Header


def main():
    testimg = File("../testImages/images.bmp")
    testimg.print_raw()
    testimg.create_header()
    print(testimg.header.width)


if __name__ == "__main__":
    main()
