from tkinter import *
from tkinter import ttk

#Structure
#personalInfo[0] = name
#personalInfo[1] = name
#personalInfo[2] = name
#personalInfo[3] = name
personalInfo = ["name","name","year","Contact Number"]

def clicked(*args):
    personalInfo[0] = a1.get()
    print(personalInfo[0])
    personalInfo[1] = b1.get()
    personalInfo[2] = c1.get()
    personalInfo[3] = d1.get()
    f = open("data.txt","w")
    f.write("Name: " + a1 + b1)
    f.write("Year: " + c1)
    f.write("Contact Number: "+ d1)
    f.close()

window = Tk()
window.title("Submit a Report")
window.geometry('400x400')
window.configure(background = "white");
#labels for all the boxes
a = Label(window ,text = "First Name").grid(row = 0,column = 0)
b = Label(window ,text = "Last Name").grid(row = 1,column = 0)
c = Label(window ,text = "Year").grid(row = 2,column = 0)
d = Label(window ,text = "Contact Number").grid(row = 3,column = 0)

#placement and entry boxes for the labels
a1 = Entry(window)
a1.grid(row = 0,column = 1)

b1 = Entry(window)
b1.grid(row = 1,column = 1)

c1 = Entry(window)
c1.grid(row = 2,column = 1)

d1 = Entry(window)
d1.grid(row = 3,column = 1)

#submit button
btn = ttk.Button(window ,text="Submit", command = clicked).grid(row=4,column=0)

#if btn == clicked :
#    f = open("data.txt","w")
#    f.write("Name: " + a1 + b1)
#    f.write("Email: " + c1)
#    f.write("Contact Number: "+ d1)
#    f.close()

window.mainloop()
