from Tkinter import *
from tkMessageBox import askokcancel


class HeaderBar (Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.logo = PhotoImage(file="images/logo.gif")
        btn = Button(self, text='Tesla', command=self.home)
        btn.grid(row=0,column=0)
        can = Canvas(self, width=100, height=100)
        can.create_image(0, 0, image=self.logo, anchor=NW)
        can.grid(row=0,column=1)
        #dropdown menu
        menu = Button(self, text='Menu', command=self.menu)
        menu.grid(row=0,column=2)
        # make a frame for menu
        self.menuFrame = Frame(self)
        text = Label(self.menuFrame, text="Hello darkness")
        text.grid(column=0, row=0)
        self.menuToggle = FALSE

    def home(self):
        ans = askokcancel('Leave your car behind','Take me home')
        if ans:
            print "Hey! Listen"
    def menu(self):
        if not self.menuToggle:
            self.menuFrame.grid(row=1, column=2)
            self.menuToggle = TRUE
        else:
            self.menuToggle=FALSE
            self.menuFrame.grid_forget()


if __name__ == '__main__':

    HeaderBar().mainloop()