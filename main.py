from func import *
from module0.class0 import *
from module1.class1 import *




def main():
    print("""Welcome to Michael Fahey's A-Level Computer Science NEA.
            
            This project is an image processing project which uses 
            matrix operations and a machine learning network to identify(classify) an image of a road sign.
            #-#-#-#-#-#-#-#-#-#-#
            """)
    # prog = Program


def test():
    testimg = Image("testImages/images.bmp")
    testimg.display("Initial Image")
    testimg.data = convolve(testimg, gaussian_kernel(5, sigma=1.2))
    testimg.display("Gaussian Blur")
    testegs = Edges(testimg)
    testegs.xedges.display("X Edges")
    testegs.yedges.display("Y Edges")
    testegs.display("Full Edges")
    testegs.nonmax()
    testegs.display("Non-Maximum Supression")
    testegs.dblthresh(0.33, 0.66)
    testegs.display("Double Thresholding")
    testegs.hysteresis()
    testegs.display("Hysteresis Tracking")





if __name__ == "__main__":
    test()
