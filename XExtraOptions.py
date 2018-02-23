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


class XInteriorOptions(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        thecar.interior = StringVar()
        self.lastChoice = "Five Seat Interior"
        # make buttons for different x interior options
        self.Seating = {
            "Five Seat Interior": 0,
            "Six Seat Interior": 6000,
            "Six Seat Interior with Center Console": 6000,
            "Seven Seat Interior": 3000
        }

        for text, value in self.Seating.iteritems():
            Radiobutton(self, text=text, variable=thecar.interior,
                        value=text, command=self.getState, indicatoron=0,
                        width=30).grid(sticky=N)
            cost = "$" + str(value)
            Label(self, text=cost).grid(sticky=N)

        self.grid()

    def getState(self):
        # check that we made a different choice, update the cost
        if (thecar.interior.get() != self.lastChoice):
            thecar.total_cost -= self.Seating[self.lastChoice]
            thecar.total_cost += self.Seating[thecar.interior.get()]
            thecar.total_cost_text.set("Total: $" + str(thecar.total_cost))
        self.lastChoice = thecar.interior.get()
        print thecar.total_cost


if __name__ == '__main__':
    XInteriorOptions(thecar)
    thecar.mainloop()
