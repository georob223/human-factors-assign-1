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
from tkMessageBox import *


class HeaderBar(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)

        # load images
        self.homeButton = PhotoImage(file="images/teslaN.gif")
        self.menuButton = PhotoImage(file="images/menuN.gif")
        self.logo = PhotoImage(file="images/logo.gif")

        #make canvas for logo image
        can = Canvas(self, width=250, height=50)
        # show the logo in a canvas
        can.create_image(125, 0, image=self.logo, anchor=N)

        # homepage button
        btn = Button(self, image=self.homeButton, command=self.home)

        # drop down menu
        menu = Menubutton(self, image=self.menuButton)

        topmenu = Menu(menu)
        topmenu.add_command(label="Help", command=self.help)
        topmenu.add_command(label="About", command=self.about)
        menu.config(menu=topmenu)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        btn.grid(row=0, column=0, sticky=W)
        menu.grid(row=0, column=1, sticky=E)
        can.grid(row=0,columnspan=5)

        self.grid(row=0, column=0, sticky=E + W)
        # print out the total so far for the car options selected.
        Label(textvariable=thecar.total_cost_text).grid(row=1, columnspan=5)

    def help(self):
        showinfo("Help", "You need to get to Wikipedia.")

    def about(self):
        showinfo("About", "Created by Rezvi Ahmed and Robbie Gascoigne")

    def home(self):
        ans = askokcancel('Leave your car behind', 'Take me home')
        if ans:
            # return to homeframe
            print "Hey! Listen"


if __name__ == '__main__':
    win = Tk()
    top = HeaderBar(win)
    win.mainloop()
