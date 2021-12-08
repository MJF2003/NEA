from module0 import class0
from module1 import class1


def valid(vtype: str, ipt, comp) -> bool:
    if vtype == "EQ":
        return ipt == comp
    elif vtype == "GT":
        return ipt > comp
    elif vtype == "LT":
        return ipt < comp
    elif vtype == "BT":
        return comp[0] < ipt < comp[1]
    elif vtype == "DG":
        return ipt.isdigit()
    else:
        return True


class Program:
    def __init__(self):
        self.fileloaded = False
        self.status = "Initialising..."
        self.option = -1
        self.menu()

    def error(self, message: str, level):  # Error Display Program
        print(message)
        if level == 3:
            self.status = "Level 3 Error..."
            self.__init__()
        elif level == 2:
            self.status = "Level 2 Error..."
        elif level == 1:
            self.status = "Level 1 Error..."
        else:
            self.status = "Unknown Error"
        print(self.status)

    def menu(self):
        menu = {
            "1": ("Load File", self.loadfile(self.getpath())),
            "2": ("Plot File", self.plotfile()),
            "3": ("Edge Detect", self.edgedetect())
        }

        for key, value in menu.items():
            print(f"{key:<5}: {value[0]:<20}")

        option = input("Enter a number from the list above: ")
        while not valid("DG", option):
            option = input("Enter a number from the list above: ")



        print(self.status)

    def getpath(self):
        pass

    def loadfile(self, path):
        pass

    def plotfile(self):
        pass

    def edgedetect(self):
        pass
