from Tkinter import *
from tkMessageBox import askokcancel


class HeaderBar (Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.logo = PhotoImage(file="images/logo.gif")
        btn = Button(self, text='Tesla', command=self.home, anchor=NW, justify=LEFT)
        btn.pack()
        can = Canvas(self, width=100, height=100)
        can.create_image(0, 0, image=self.logo, anchor=NW)
        can.pack(anchor=N)

    def home(self):
        ans = askokcancel('Leave your car behind','Take me home')
        if ans:
            print "Hey! Listen"


if __name__ == '__main__':

    HeaderBar().mainloop()