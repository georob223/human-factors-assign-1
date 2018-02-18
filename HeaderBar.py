from Tkinter import *
from tkMessageBox import askokcancel


class HeaderBar (Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        Grid.rowconfigure(self,0,weight=1)
        Grid.columnconfigure(self, 0, weight=1)
        Grid.columnconfigure(self, 1, weight=1)
        Grid.columnconfigure(self, 2, weight=1)
        self.grid()
        self.logo = PhotoImage(file="images/logo.gif")
        btn = Button(self, text='Tesla', command=self.home)
        btn.grid(row=0, column=0, sticky=NW)
        can = Canvas(self, width=250, height=50)
        can.create_image(125, 0, image=self.logo, anchor=N)
        can.grid(row=0, column=1)
        # drop down menu
        menu = Button(self, text='Menu', command=self.menu)
        menu.grid(row=0, column=2, sticky=NE)
        # make a frame for menu
        self.menuFrame = Frame(self)
        text = Label(self.menuFrame, text="Hello darkness")
        text.grid(column=0, row=0, sticky=N)
        self.menuToggle = FALSE

    def home(self):
        ans = askokcancel('Leave your car behind', 'Take me home')
        if ans:
            # return to homeframe
            print "Hey! Listen"

    def menu(self):
        if not self.menuToggle:
            self.menuFrame.grid(row=1, column=2, sticky=N)
            self.menuToggle = TRUE
        else:
            self.menuToggle = FALSE
            self.menuFrame.grid_forget()


if __name__ == '__main__':
    win = Tk()
    top = HeaderBar(win)
    win.mainloop()