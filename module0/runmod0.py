from class0 import File, Header


def main():
    myFile = File("../data/30.bmp")
    print(myFile.header)


if __name__ == "__main__":
    main()