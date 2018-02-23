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


class PowerRange(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.sd75desImage = PhotoImage(file="images/75ddes.gif")
        self.sd100desImage = PhotoImage(file="images/s100ddes.gif")
        self.spd100desImage = PhotoImage(file="images/sp100ddes.gif")

        sd75 = Button(self, image=self.sd75desImage, command=self.select75d)
        sd75.grid(row=1, column=0)
        sd100 = Button(self, image=self.sd100desImage, command=self.select100d)
        sd100.grid(row=1, column=1)
        sp100d = Button(self, image=self.spd100desImage, command=self.selectP100d)
        sp100d.grid(row=1, column=2)
        self.grid()

    def select75d(self):
        thecar.power = "75D"

    def select100d(self):
        thecar.power = "100D"

    def selectP100d(self):
        thecar.power = "P100D"


if __name__ == '__main__':
    win = Tk()
    top = PowerRange(win)
    win.mainloop()
