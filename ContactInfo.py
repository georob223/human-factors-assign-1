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

from Globals import *
import tkFont


class ContactInfo(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        # setup for the grid to expanding maybe

        times20B = tkFont.Font(family='Times', size=20, weight=tkFont.BOLD)
        arial12 = tkFont.Font(family='Arial', size=10)

        contactLbl = Label(self, text="Contact Information", font=times20B)
        contactLbl.grid(row=1, column=0, sticky=W)
        firstNameLbl = Label(self, text="First Name:")
        firstNameLbl.grid(row=2, column=0, sticky=W)
        lastNameLbl = Label(self, text="Last Name:")
        lastNameLbl.grid(row=3, column=0, sticky=W)
        phoneNumberLbl = Label(self, text="Phone:")
        phoneNumberLbl.grid(row=4, column=0, sticky=W)
        emailAddrLbl = Label(self, text="E-mail:")
        emailAddrLbl.grid(row=5, column=0, sticky=W)
        addressLbl = Label(self, text="Address:")
        addressLbl.grid(row=6, column=0, sticky=W)
        cityLbl = Label(self, text="City:")
        cityLbl.grid(row=7, column=0, sticky=W)
        state_provLbl = Label(self, text="State:")
        state_provLbl.grid(row=8, column=0, sticky=W)
        countryLbl = Label(self, text="Country:")
        countryLbl.grid(row=9, column=0, sticky=W)
        zipCodeLbl = Label(self, text="Zip:")
        zipCodeLbl.grid(row=10, column=0, sticky=W)

        firstNameEnt = Entry(self, textvariable=thebuyer.firstName)
        firstNameEnt.grid(row=2, column=1, sticky=W)
        lastNameEnt = Entry(self, textvariable=thebuyer.lastName)
        lastNameEnt.grid(row=3, column=1, sticky=W)
        phoneEnt = Entry(self, textvariable=thebuyer.phone)
        phoneEnt.grid(row=4, column=1, sticky=W)
        emailEnt = Entry(self, textvariable=thebuyer.email)
        emailEnt.grid(row=5, column=1, sticky=W)
        addressEnt = Entry(self, textvariable=thebuyer.address)
        addressEnt.grid(row=6, column=1, sticky=W)
        cityEnt = Entry(self, textvariable=thebuyer.city)
        cityEnt.grid(row=7, column=1, sticky=W)
        stateEnt = Entry(self, textvariable=thebuyer.state_prov)
        stateEnt.grid(row=8, column=1, sticky=W)
        countryEnt = Entry(self, textvariable=thebuyer.country)
        countryEnt.grid(row=9, column=1, sticky=W)
        zipEnt = Entry(self, textvariable=thebuyer.zip)
        zipEnt.grid(row=10, column=1, sticky=W)
        self.grid()


if __name__ == '__main__':
    win = Tk()
    top = ContactInfo(win)
    win.mainloop()
