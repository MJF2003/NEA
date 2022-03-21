from module0.class0 import *
from module1.class1 import *
from module2.class2 import *

from UI.pys.template import *
from PyQt5.QtWidgets import *

import sys
import numpy as np
import PIL.Image



def main():
    app = QApplication(sys.argv)

    window = QDialog()
    ui = Ui_templateScreen()
    ui.setupUi(window)

    window.show()
    sys.exit(app.exec_())


def full_edges(path):
    img = Image(path)
    img.data = convolve(img, gaussian_kernel(5, sigma=1.2))
    edges = Edges(img)
    edges.nonmax()
    edges.dblthresh(0.3, 0.3)
    edges.hysteresis()
    edges.invert()
    return edges


def test():
    testimg = Image("data/classified/thirtymph/101.bmp")
    testimg.display("Initial Image")
    testimg.data = convolve(testimg, gaussian_kernel(5, sigma=1.2))
    testimg.display("Gaussian Blur")
    testegs = Edges(testimg)
    testegs.xedges.display("X Edges")
    testegs.yedges.display("Y Edges")
    testegs.display("Full Edges")
    testegs.nonmax()
    testegs.display("Non-Maximum Supression")
    testegs.dblthresh(0.3, 0.3)
    testegs.display("Double Thresholding")
    testegs.hysteresis()
    testegs.display("Hysteresis Tracking")
    testegs.invert()
    testegs.display("Inverted")


    # rawimg = PIL.Image.open("testImages/")

    img = np.array(testegs.data)
    img = np.resize(img, (100, 100, 3))
    img = tf.expand_dims(img, 0)


    pred_img(img, load_model('my_model'), my_classes)




if __name__ == "__main__":
    test()
