from Tkinter import *
from Globals import *

class FooterButtons (Frame):
    def __init__(self, next_func, last_func, parent=None, next_text="Next", last_text="Previous"):
        Frame.__init__(self, parent)
        Button(self,text=next_text, command=self.nextActivate).grid(row=0, column=1)
        Button(self,text=last_text, command=self.lastActivate).grid(row=0, column=0)
        self.grid()
        self.next=next_func
        self.last=last_func
    #calls the next section of the app
    def nextActivate(self):
        self.grid_forget()
        self.next()
    #returns to the last section of the app
    def lastActivate(self):
        self.grid_forget()
        self.last()
