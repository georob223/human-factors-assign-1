from Tkinter import *
from HeaderBar import HeaderBar
from Paint import FooterButtons

HeaderBar().activate()
toot = FooterButtons(HeaderBar().activate,HeaderBar().activate,parent=None)
toot.mainloop()
