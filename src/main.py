from func import *
from module2.class2 import *
from module1.class1 import *
from module0.class0 import *

import numpy as np


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
    img = np.array(full_edges("testImages/30mph.bmp").data)
    img = np.resize(img, (100, 100, 3))
    img = tf.expand_dims(img, 0)

    train(*build_model(Path('data/classified_edges')), save_loc='my_model', epochs=55)

    print(pred_img(img, load_model(Path('my_model')), class_names))


class Program:
    def __init__(self):
        self.fileloaded : Image = Image(None)
        self.Edges = False
        self.log = ["Initialising..."]
        self.option = -1
        self.menu_dict = {  # Menu of all testing interface functions
            "1": ("Load File", self.pg_loadfile),
            "2": ("Plot File", self.pg_plotfile),
            "3": ("Gaussian Blur", self.pg_gauss),
            "4": ("Non-max suppression", self.pg_nonmax),
            "5": ("Double Thresholding", self.pg_double_thresh),
            "6": ("Hysteresis Tracking", self.pg_hysteresis),
            "7": ("Invert Edges", self.pg_invert),
            "8": ("Full Edge Detection", self.pg_fulledge),
            "9": ("Generate ASCII Art", self.pg_asciiart),
            "10": ("Train ML Model", self.pg_train),
            "11": ("Predict Road Sign type", self.pg_predict),
            "12": ("Setup a multistage run", self.pg_multistep),
            "13": ("Print program log", self.print_log),
            "14": ("Exit the Program", self.exit)
        }
        self.menu()  # Display menu upon program initialising

    def error(self, message: str, status: str, level: int):  # Error Display Program
        print(message)
        if level == 1:  # 1 indicates a fatal error causing the program to reset. Otherwise, it just adds it to the log
            print("RESTARTING...")
            self.log.append(f"Fatal Error - {status}")
            self.__init__()
        else:
            self.log.append(f"Error caused by {status}")


    def get_path(self, path_from_root):  # Any system file path handler
        root = Path(__file__).parent.parent
        file_path = root / Path(path_from_root)
        print(file_path)
        if file_path.exists():
            return file_path
        else:
            return "BadPath"


    def menu(self):
        print("\n")
        for key, value in self.menu_dict.items():
            print(f"{key:<5}: {value[0]:<20}")
        print("\n")

        self.option = input("Enter a number from the list above: ")
        while not valid("DG", self.option):
            self.error("That wasn't a number", "User Fault", status=0)
            self.option = input("Enter a number from the list above: ")
        #try:
        self.menu_dict[self.option][1]()
        #except:
        #    self.error("Unknown Fatal Error occured", "Unknown Runtime Error", 1)
        if not self.option == -1:
            self.menu()

    # Menu Function Handler #

    def pg_loadfile(self):
        if self.fileloaded.filename is not None:
            fl_check = input("File is already loaded. "
                             "Loading will overwrite the file currently loaded.\nDo you want to continue (Y/N)? ")
            try:
                if fl_check.upper() != "Y":
                    return None
            except ValueError:
                self.error("Non-String was entered", "Input Error", 0)
                return None
        while 1:
            intended_path = self.get_path(
                input("Enter the path of the file you would like to load referenced from the NEA root "
                      "folder: "))
            if intended_path == "BadPath":
                self.error("File does not exist", "File Existence", 0)
            elif intended_path.suffix != '.bmp':
                self.error("File is of wrong type", "File Type", 0)
            else:
                self.fileloaded = Image(intended_path)
                print("File was loaded!")
                break


    def pg_plotfile(self):
        if not self.fileloaded:
            self.error("File has not been loaded", "Sequence Error", 0)
            return None
        self.fileloaded.display("Raw Loaded Image")

    def pg_asciiart(self):
        pass

    def pg_gauss(self):
        pass

    def pg_nonmax(self):
        pass

    def pg_double_thresh(self):
        pass

    def pg_hysteresis(self):
        pass

    def pg_invert(self):
        pass

    def pg_fulledge(self):
        pass

    def pg_train(self):
        pass

    def pg_predict(self):
        pass

    def pg_multistep(self):
        pass

    def print_log(self):
        print("Program log is as follows:")
        for errno, error in enumerate(self.log):
            print(f"{errno}) - {error:<20}")

    def exit(self):
        self.option = -1


def main():
    welcome = """
            Hello and welcome to the testing interface for my Computer Science Coursework 2022.
            I am Michael Fahey (7407) and my NEA is all about detecting road signs. 
            
            You can see the full writeup on my GitHub. I obviously hope everything works but please raise an issue
            on the repo if you come across anything not working."""
    print(welcome)
    prog = Program()
    print("Thank you for using the program - Michael")


if __name__ == "__main__":
    main()
