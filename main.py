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
    testimg = Image("testImages/images.bmp")
    testimg.display()
    testimg.data = convolve(testimg, gaussian_kernel(5, sigma=1))
    testimg.display()
    testegs = Edges(testimg)
    testegs.xedges.display()
    testegs.yedges.display()
    testegs.display()






if __name__ == "__main__":
    test()
