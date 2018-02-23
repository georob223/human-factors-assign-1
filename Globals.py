from Tkinter import *
# *****************************************************************************
# *****     Students: Robbie Gascoigne, Rezvi Ahmed                       *****
# *****        Class: Human Factors and User Interface                    *****
# *****   Instructor: Gamradt                                             *****
# *****   Assignment: 1                                                   *****
# *****     Due Date: 02-23-18                                            *****
# *****************************************************************************
# *****   Description: This program allows the selction of options on a   *****
# *****   Tesla, for the Model S and Model X. It uses Tkinter from Python *****
# *****   2.7 and the widgets contained in each. In this case, we use     *****
# *****   a variety of frame based classes to have compartmentelized code *****
# *****   for each sub piece of the car.                                  *****
# *****************************************************************************

class Car(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.paint = "Pearl White Multi-Coat"
        self.options = StringVar()
        self.total_cost = 0
        self.total_cost_text = StringVar()
        self.model = ""
        self.power = ""
        self.interior = StringVar()

    def checkvar(self):
        print self.paint
        print self.options
        print self.total_cost
        print self.model
        print self.power
        print self.extra_options


class Buyer():
    def __init__(self):
        self.address = ""
        self.city = ""
        self.state_prov = ""
        self.country = ""
        self.zip = ""
        self.firstName = ""
        self.lastName = ""
        self.phone = ""
        self.email = ""


thecar = Car()
thebuyer = Buyer()
