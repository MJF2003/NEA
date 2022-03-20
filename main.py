from func import *
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
    edges.dblthresh(0.3, 0.45)
    edges.hysteresis()
    edges.invert()
    return edges


def test():
    testimg = Image("testImages/myNSL.bmp")
    testimg.display("Initial Image")
    testimg.data = convolve(testimg, gaussian_kernel(5, sigma=1.2))
    testimg.display("Gaussian Blur")
    testegs = Edges(testimg)
    testegs.xedges.display("X Edges")
    testegs.yedges.display("Y Edges")
    testegs.display("Full Edges")
    testegs.nonmax()
    testegs.display("Non-Maximum Supression")
    testegs.dblthresh(0.3, 0.45)
    testegs.display("Double Thresholding")
    testegs.hysteresis()
    testegs.display("Hysteresis Tracking")
    testegs.invert()
    testegs.display("Inverted")

    model, train_ds, val_ds, class_names = build_model()

    epochs = 50
    history = model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=epochs
    )

    # rawimg = PIL.Image.open("testImages/nsl_test.png")

    img = np.array(testegs.data)
    img = np.resize(img, (48, 48, 3))
    img = tf.expand_dims(img, 0)


    predictions = model.predict(img)
    score = tf.nn.softmax(predictions[0])
    print(score)

    print(
        f"""This image most likely belongs to {class_names[np.argmax(score)]} 
        with a {100 * np.max(score):.2f} percent confidence."""
    )


if __name__ == "__main__":
    test()
