from src.module2.class2 import *
from src.module1.class1 import *
from src.module0.class0 import *
from src.func import *
from colorama import Fore, Back, Style

import numpy as np
import copy


class Program:
    """
    Main Program Class is a class which describes how the main program should run
    OOP has been used as it allows the use of variables protected by the class, which can be accessed by all methods
    in the program class responsible for running the program. It also allows functions specfic to the program run,
    to access and manipulate attributes such as the log and loaded file.
    """
    def __init__(self):
        """
        Sets up inital values of runtime attributes as well as calling the menu function when the program is
        instantiated
        """
        self.fileloaded = False
        self.original = None
        self.model_trained = False
        self.file = None
        self.log = ["Initialising..."]
        self.option = -1
        self.menu_dict = {  # Menu of all testing interface functions
            "1": ("Load File", self.pg_loadfile),
            "2": ("Plot File", self.pg_plotfile),
            "3": ("Gaussian Blur", self.pg_gauss),
            "4": ("Apply Sobel Filters", self.pg_sobel),
            "5": ("Non-max suppression", self.pg_nonmax),
            "6": ("Double Thresholding", self.pg_double_thresh),
            "7": ("Hysteresis Tracking", self.pg_hysteresis),
            "8": ("Invert Edges", self.pg_invert),
            "9": ("Full Edge Detection", self.pg_fulledge),
            "10": ("Generate ASCII Art", self.pg_asciiart),
            "11": ("Train ML Model", self.pg_train),
            "12": ("Predict Road Sign type", self.pg_predict),
            "13": ("Setup a multistage run", self.pg_multistep),
            "14": ("Print program log", self.print_log),
            "15": ("Exit the Program", self.exit)
        }
        self.menu()  # Display menu upon program initialising

    def error(self, message: str, status: str, level: int):  # Error Display Program
        """
        General Error display and handler for program runtime
        :param message: Message to be displayed to the user
        :param status: Message to be added to the log
        :param level: Error severity - does the program need to be reset
        :return: None
        """
        print(Fore.BLACK + Back.RED + message + Fore.RESET + Back.RESET)
        if level == 1:  # 1 indicates a fatal error causing the program to reset. Otherwise, it just adds it to the log
            print("RESTARTING...")
            self.log.append(f"Fatal Error - {status}")
            self.__init__()
        else:
            self.log.append(f"Error caused by {status}")

    def menu(self):
        """
        Prints the menu to the user as well as handling choice flow.
        :return: None
        """
        for key, value in self.menu_dict.items():  # Print out menu
            print(Fore.WHITE + Back.BLACK + f"{key:<5}: {value[0]:<25}" + Fore.RESET + Back.RESET)

        self.option = input("Enter a number from the list above: ")
        while not (valid("DG", self.option) and valid("BT", self.option, comp=(0, 16))):  # Validaiton check
            self.error("That wasn't a valid number", "User Fault", 0)
            self.option = input("Enter a number from the list above: ")
        try:
            self.log.append(self.option)
            self.menu_dict[self.option][1]()
        except:  # Allows program to crash out without any red text
            self.error("Unknown Fatal Error occured", "Unknown Runtime Error", 1)
        if not self.option == -1:
            self.menu()

    # Menu Function Handler #

    def pg_loadfile(self):
        """
        Manages UX for loading an image file into the program and saving it to a program variable
        :return: None
        """
        if self.fileloaded is not False:
            fl_check = input("File is already loaded. "
                             "Loading will overwrite the file currently loaded.\nDo you want to continue (Y/N)? ")
            if fl_check.upper() != "Y":
                return None
        while 1:
            intended_path = get_path(
                input("Enter the path of the file you would like to load referenced from the NEA root "
                      "folder: "))
            if not intended_path.exists():
                print(f"You directed to {intended_path}")
                self.error("File does not exist", "File Existence", 0)
            elif intended_path.suffix != '.bmp':
                self.error("File is of wrong type", "File Type", 0)
            else:
                self.original = Edges(Image(intended_path))
                self.file = Edges(Image(intended_path))
                print("File was loaded!")
                self.log.append("NEW_FILE")
                self.fileloaded = True
                break


    def pg_plotfile(self):
        """
        Manages UX for plotting the loaded file to screen using matplotlib.
        Requires file to be loaded first.
        :return: None
        """
        if self.fileloaded is False:
            self.error("File has not been loaded", "Sequence Error", 0)
            return None
        self.file.display("Raw Loaded Image")
        print("File displayed")

    def pg_asciiart(self):
        """
        Manages UX for generating ASCII Art of the loaded file.
        Requires file to be loaded first.
        :return: None
        """
        if self.fileloaded is False:
            self.error("File has not been loaded", "Sequence Error", 0)
            return None
        self.file.asciiart(get_path('src/ascii'))
        print("ASCII art Generated!")

    def pg_gauss(self):
        """
        Manages UX for applying and displaying outcome of Gaussian Blur.
        Requires file to be loaded first.
        :return: None
        """
        if self.fileloaded is False:
            self.error("File has not been loaded", "Sequence Error", 0)
            return None
        self.file.gaussian_blur()
        self.file.display("Post Gaussian Blur")
        print("Gaussian Blur Applied!")

    def pg_sobel(self):
        """
        Manages UX for applying and displaying outcome of Sobel Filters.
        Requires file to be loaded first.
        :return: None
        """
        if self.fileloaded is False:
            self.error("File has not been loaded", "Sequence Error", 0)
            return None
        self.file.apply_sobel()
        self.file.display("Post Sobel Filters")
        print("Sobel Filters Applied!")

    def pg_nonmax(self):
        """
        Manages UX for applying and displaying outcome of applying non-maximum suppression
        Requires file to be loaded and Sobel filters to be applied
        :return: None
        """
        if self.fileloaded is False:
            self.error("File has not been loaded", "Sequence Error", 0)
            return None
        elif "4" not in "".join(self.log).split("NEW_FILE")[-1]:  # Checks a Sobel has happened since last file load
            print("".join(self.log).split("NEW_FILE")[-1])
            self.error("Sobel Filters not yet applied", "Sequence Error", 0)
            self.log.pop()
            return None
        self.file.nonmax()
        self.file.display("Post Non Maximum Supression")
        print("NMS Applied!")

    def pg_double_thresh(self):
        """
        Manages UX for applying and displaying outcome of applying double thresholding.
        Requires file to be loaded, Sobel filter to be applied and Non-Max Suppression to be applied.
        :return: None
        """
        if self.fileloaded is False:
            self.error("File has not been loaded", "Sequence Error", 0)
            return None
        # Checks conditions have happened since last file load
        elif "5" not in "".join(self.log).split("NEW_FILE")[-1]:
            self.error("NMS not yet applied", "Sequence Error", 0)
            self.log.pop()
            return None
        self.file.dblthresh(0.27, 0.35)
        self.file.display("Post Double Thresholding")
        print("Double Thresholding Applied!")

    def pg_hysteresis(self):
        """
        Manages UX for applying and displaying outcome of applying hysteresis tracking.
        Requires file to be loaded, Sobel, NMS and Double Thresholding to be applied.
        :return: None
        """
        if self.fileloaded is False:
            self.error("File has not been loaded", "Sequence Error", 0)
            return None
        # Checks conditions have happened since last file load
        elif "6" not in "".join(self.log).split("NEW_FILE")[-1]:
            self.error("DBL Threshold not yet applied", "Sequence Error", 0)
            self.log.pop()
            return None
        self.file.hysteresis()
        self.file.display("Post Hysteresis Tracking")
        print("Hysteresis Tracking Applied!")

    def pg_invert(self):
        """
        Manages UX for applying and displaying outcome of inverting the edges in the image.
        Requires file to be loaded and edge detection to have been run.
        :return: None
        """
        if self.fileloaded is False:
            self.error("File has not been loaded", "Sequence Error", 0)
            return None
        # Checks conditions have happened since last file load
        elif "7" not in "".join(self.log).split("NEW_FILE")[-1]:
            self.error("Hysteresis not yet applied", "Sequence Error", 0)
            self.log.pop()
            return None
        self.file.invert()
        self.file.display("Inverted Edges")
        print("Edges inverted!")

    def pg_fulledge(self):
        """
        Manages UX for applying full edge detection to a loaded image and displaying the final outcome to the user.
        Requires file to be loaded.
        :return: None
        """
        if self.fileloaded is False:
            self.error("File has not been loaded", "Sequence Error", 0)
            return None
        lcl_file = copy.deepcopy(self.file)
        lcl_file.gaussian_blur()
        lcl_file.apply_sobel()
        lcl_file.nonmax()
        lcl_file.dblthresh(0.27, 0.35)
        lcl_file.hysteresis()
        lcl_file.hysteresis()
        lcl_file.invert()
        lcl_file.display("Output")
        choice = input("Would you like to use these detected edges further in the program? (Y/N): ")
        if choice.upper() == "Y":
            self.file = lcl_file
            print("Edges Saved")
        else:
            print("Edges Discarded")

    def pg_train(self):
        """
        Manages UX for training a machine learning model.
        :return: None
        """
        if get_path("src/my_model").exists():
            self.model_trained = True
        if self.model_trained:
            print("Trained model exists. Training will overwrite the saved model")
            choice = input("Do you want to continue? (Y/N) ")
            if choice.upper() != "Y":
                print("Okay. Aborting training function")
                return None
        train(*build_model(get_path("src/data/classified")), save_loc=get_path("src/my_model"), epochs=55)
        self.model_trained = True
        print("Model was trained!")

    def pg_predict(self):
        """
        Manages UX for predicting the class of an image of unseen data based on a trained model.
        :return: None
        """
        if get_path("src/my_model").exists():
            self.model_trained = True
        if self.fileloaded is False:
            self.error("File has not been loaded", "Sequence Error", 0)
            return None
        elif not self.model_trained:
            self.error("No trained model present. Run function \"Train\"", "Sequence Error", 0)
        try:
            img = np.array(self.original.data)
            img = np.resize(img, (100, 100, 3))
            img = tf.expand_dims(img, 0)
            result = pred_img(img, load_model(Path('src/my_model')), class_names)
            print(result[1])
        except:
            self.error("Program was unable to predict on this image", "ML Nonsense Error", 1)

    def pg_multistep(self):
        """
        Manages UX for building a queue of functions to run in sequence.
        No prerequisites.
        :return: None
        """
        print("Starting Multistep Assembler!")
        queue = []
        stop = False
        while not stop:
            select = input("Enter a function option from the list: ")
            # Validity check on user input
            if not (valid("DG", select) and valid("BT", select, comp=(0, 16))):
                self.error("Entry was not valid", "User Fault", 0)
                continue
            elif valid("EQ", select, comp="13"):
                self.error("Cannot add multistep as part of multistep", "User Fault", 0)
            else:
                queue.append((select, self.menu_dict[select][1]))
            if input("Would you like to add more functions? (Y/N): ").upper() != "Y":
                stop = True
                for function in queue:
                    self.log.append(function[0])  # Appends function number to program log
                    function[1]()  # Runs indicated funtion

    def print_log(self):
        """
        Prints the program log to the user screen
        :return: None
        """
        print("Program log is as follows:")
        for errno, error in enumerate(self.log):
            print(f"{errno}) - {error:<25}")

    def exit(self):
        """
        Exits program class completely
        :return:
        """
        self.option = -1


def main():
    """
    Prints welcome and exit messages and instantiates the main program class
    :return:
    """
    welcome = """
            Hello and welcome to the testing interface for my Computer Science Coursework 2022.
            I am Michael Fahey (7407) and my NEA is all about detecting road signs. 
            
            You can see the full writeup on my GitHub. I obviously hope everything works but please raise an issue
            on the repo if you come across anything not working.
            

"""
    os.system('cls' if os.name == 'nt' else 'clear')  # Clears current screen completely
    print(Fore.BLACK + Back.GREEN + Style.BRIGHT + welcome + Style.RESET_ALL)
    prog = Program()
    print("Thank you for using the program - Michael")


if __name__ == "__main__":
    main()
