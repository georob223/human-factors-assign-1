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

class Home (Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.modelXImage = PhotoImage(file="images/modelX.gif")
        self.modelSImage = PhotoImage(file="images/modelS.gif")

        modelsButton = Button(self,text="Model S\nElectric Sedan",
                              image=self.modelSImage, compound=TOP,
                              command=self.modelS)
        modelsButton.grid(row=1, column=0, sticky=W)
        modelxButton = Button(self,text="Model X\nElectric SUV",
                              image=self.modelXImage, compound=TOP,
                              command=self.modelX)
        modelxButton.grid(row=1, column=2,sticky=E)
        self.grid()
    def modelS(self):
        self.model = "Model S"
    def modelX(self):
        self.model = "Model X"

if __name__ == '__main__':
    win = Tk()
    top = Home(win)
    win.mainloop()
