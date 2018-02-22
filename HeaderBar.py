from Tkinter import *
from tkMessageBox import *
from Globals import *

class HeaderBar (Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
    def activate(self):
        # setup for the grid to expanding maybe
        Grid.rowconfigure(self, 0, weight=1)
        Grid.columnconfigure(self, 0, weight=1)
        Grid.columnconfigure(self, 1, weight=1)
        Grid.columnconfigure(self, 2, weight=1)
        self.grid()
        # load the logo
        self.logo = PhotoImage(file="images/logo.gif")
        # homepage button
        btn = Button(self, text='Tesla', command=self.home)
        btn.grid(row=0, column=0, sticky=NW)
        can = Canvas(self, width=250, height=50)
        # show the logo in a canvas
        can.create_image(125, 0, image=self.logo, anchor=N)
        can.grid(row=0, column=1)
        # drop down menu
        menu = Menubutton(self, text='Menu')
        menu.grid(row=0, column=2, sticky=NE)
        topmenu = Menu(menu)
        topmenu.add_command(label="Help", command=self.help)
        topmenu.add_command(label="About", command=self.about)
        menu.config(menu=topmenu)
    def help(self):
        showinfo("Help", "You need to get to Wikipedia.")
    def about(self):
        showinfo("About","Created by Rezvi Ahmed and Robbie Gascoigne")
    def home(self):
        ans = askokcancel('Leave your car behind', 'Take me home')
        if ans:
            # return to homeframe
            print "Hey! Listen"





if __name__ == '__main__':
    win = Tk()
    top = HeaderBar(win)
    win.mainloop()