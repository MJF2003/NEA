from func import *
from module0.class0 import *
from module1.class1 import *
from module2.class2 import *


def main():
    print(
        """
        Welcome to Michael Fahey's A-Level Computer Science NEA.
        
        This project is an image processing project which uses 
        matrix operations and a machine learning network to identify(classify) an image of a road sign.
        #-#-#-#-#-#-#-#-#-#-#
        """
    )
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
    epochs = 10
    history = model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=epochs
    )

    img = np.ndarray(testegs.data).resize((100, 100))
    img_array = tf.expand_dims(img, 0)  # Create a batch

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    print(
        "This image most likely belongs to {} with a {:.2f} percent confidence."
            .format(class_names[np.argmax(score)], 100 * np.max(score))
    )





if __name__ == "__main__":
    test()
