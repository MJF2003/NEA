from func import *
from module0.class0 import *
from module1.class1 import *



def main():
    print("""Welcome to Michael Fahey's A-Level Computer Science NEA.
            
            This project is an image processing project which uses 
            matrix operations and a machine learning network to identify(classify) an image of a road sign.
            #-#-#-#-#-#-#-#-#-#-#
            """)
    prog = Program


def test():
    testimg = Image("testImages/sdjm.bmp")
    testimg.display()
    # testimg.asciiart()
    gausskn = gaussian_kernel(7, sigma=1)
    print(gausskn.data)
    testimg.convolve(gausskn)
    testimg.display()
    testimg.asciiart()



if __name__ == "__main__":
    test()
