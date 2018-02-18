from Tkinter import *
from tkMessageBox import askokcancel


class HeaderBar (Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        logo = PhotoImage(file='images/logo.gif')
        can = Canvas(self)
        can.pack(fill=BOTH)
        can.config(width=20, height=20)
        can.create_image(0, 0, image=logo, anchor=N)
        btn = Button(self, text='Tesla', command=self.home)
        btn.pack(fill=BOTH)

    def home(self):
        ans = askokcancel('Leave your car behind','Take me home')
        if ans:
            print "Hey! Listen"


if __name__ == '__main__':

    HeaderBar().mainloop()