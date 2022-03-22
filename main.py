from module0.class0 import *
from module1.class1 import *
from module2.class2 import *
from func import *

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
    edges.dblthresh(0.25, 0.27)
    edges.hysteresis()
    edges.hysteresis()
    edges.invert()
    edges.display("Output")
    return edges


def test():
    # rawimg = PIL.Image.open("testImages/myNSL.bmp")
    img = np.array(full_edges("testImages/myNSL.bmp").data)
    img = np.resize(img, (100, 100, 3))
    img = tf.expand_dims(img, 0)

    train(*build_model(), save_loc='my_model')

    print(pred_img(img, load_model('my_model'), get_classes()))



if __name__ == "__main__":
    test()
