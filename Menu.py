from MenuOption import *

class Menu:

    def __init__(self):
        self.choices = [
        ("exit", exit)
        ]

    def addOption(self, menuOption):

        self.choices.append((menuOption.name, menuOption.change))

    def chooseOption(self, menuOptionNum):


        if menuOptionNum >= 0 and menuOptionNum < len(self.choices):
            self.choices[menuOptionNum][1]()
        else:
            print("Non-valid input")

    
