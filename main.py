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

from XExtraOptions import *
from HeaderBar import *
from Paint import *
from Options import Options
from PowerRange import PowerRange
from Home import *
from ContactInfo import *
from ttk import *

# each item can be called via a button, or otherwise as needed
# thecar is defined in Globals.py, and acts as our common information
# need to erase settings if we change model of the car


HeaderBar(thecar)
stuff = Notebook()
stuff.add(Home(), text="Home")
stuff.add(PowerRange(), text="Power")
stuff.add(Paint(), text="Paint")
stuff.add(Options(), text="Options")
stuff.add(XInteriorOptions(), text="Interior Options")
stuff.add(ContactInfo(), text="Contact")

stuff.grid()

thecar.mainloop()
