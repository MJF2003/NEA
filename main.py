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
    testimg = Image("testImages/30mph.bmp")
    testimg.display("Initial Image")
    testimg.data = convolve(testimg, gaussian_kernel(5, sigma=1.2))
    testimg.display("Gaussian Blur")
    testegs = Edges(testimg)
    testegs.xedges.display("X Edges")
    testegs.yedges.display("Y Edges")
    testegs.display("Full Edges")
    testegs.nonmax()
    testegs.display("Non-Maximum Supression")
    testegs.dblthresh(0.33, 0.55)
    testegs.display("Double Thresholding")
    testegs.hysteresis()
    testegs.display("Hysteresis Tracking")
    for y in range(testegs.height):
        for x in range(testegs.width):
            testegs.data[y][x] = 1 - testegs.data[y][x]
    testegs.display("Inverted")





if __name__ == "__main__":
    test()
