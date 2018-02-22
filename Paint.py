from Tkinter import *
from Globals import *
from FooterButtons import *

class PowerFrame(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
    def activate(self):
        but = Button(self, text="Idk bro")
        but.grid(row=0, column=1)
        self.grid()

if __name__ == '__main__':
    toots = FooterButtons(PowerFrame().activate,PowerFrame().activate, None, "Power","Model")
    toots.mainloop()