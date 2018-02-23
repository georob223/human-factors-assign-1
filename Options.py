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

from Globals import *


class Options(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        # holds check button state
        self.varoptions = []
        # used for identifing what changed in state
        self.lastoptions = [0, 0, 0]
        # make buttons for different options
        self.Options = [
            ("Premium Upgrades Package", 6000),
            ("Enhanced Autopilot", 5000),
            ("Full Self-Driving Capability", 3000)
        ]

        for text, value in self.Options:
            var = IntVar()
            #make the print version with a dollar sign
            printvalue = "$" + str(value)
            Checkbutton(self, text=text, variable=var, command=self.getState,
                        width=30).grid(sticky=N)
            #simple label for the price of the feature
            Label(self, text=printvalue).grid(sticky=N)
            self.varoptions.append((value, var))

        self.grid()

    def getState(self):
        # should also set which option strings are actually applied
        # gonna leave it to future versions
        length = 0
        for value, intvar in self.varoptions:
            # did the state change from last time? which var?
            if intvar.get() != self.lastoptions[length]:
                print "doot!"
                # check to see if value is 0 or 1, increment if 1,
                # decrement if zero
                if (intvar.get() == 1):
                    # increment value of options because it is new
                    thecar.total_cost += self.Options[length][1]
                else:
                    # decrement the cost of value
                    thecar.total_cost -= self.Options[length][1]
                # update our printable textvar
                thecar.total_cost_text.set("Total: $" + str(thecar.total_cost))
                # set the last option to the current value
                self.lastoptions[length] = intvar.get()
            # increment our counter var
            length += 1


if __name__ == '__main__':
    win = Tk()
    Options(win)
    win.mainloop()
