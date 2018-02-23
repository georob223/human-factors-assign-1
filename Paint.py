from Globals import *

class Paint(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.paint = StringVar()
        self.lastpaint = "Solid Black"
        # make buttons for different paint colors
        self.Colors = {
            "Red Multi-Coat":1500,
            "Pearl White Multi-Coat":1500,
            "Silver Metallic":1000,
            "Deep Blue Metallic":1000,
            "Obsidian Black Metallic":1000,
            "Midnight Silver Metallic":1000,
            "Solid Black":0
        }

        for text, value in self.Colors.iteritems():
            Radiobutton(self, text=text, variable=self.paint, value=text, command=self.getState,
                        indicatoron=0, width=20).grid(sticky=N)
            cost = "$" + str(value)
            Label(self, text=cost).grid(sticky=N)

        self.grid()
    def getState(self):
        # check that we made a different choice, update the cost
        if (self.paint.get() != self.lastpaint):
            thecar.total_cost -= self.Colors[self.lastpaint]
            thecar.total_cost += self.Colors[self.paint.get()]
            #set the paint
            thecar.paint= self.paint.get()
            #update the current paint
            self.lastpaint = self.paint.get()
            #update text var total for display
            thecar.total_cost_text.set("Total: $" + str(thecar.total_cost))

if __name__ == '__main__':
    Paint(thecar)
    thecar.mainloop()

