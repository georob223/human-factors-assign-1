from Tkinter import *
from HeaderBar import HeaderBar
from Paint import *
from FooterButtons import *

HeaderBar().activate()
toot = FooterButtons(HeaderBar().activate,HeaderBar().activate,parent=None)
toot.mainloop()
