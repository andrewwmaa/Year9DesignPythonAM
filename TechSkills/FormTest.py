from tkinter import *
from tkinter import ttk

#Structure
#personalInfo[0] = name
#personalInfo[1] = name
#personalInfo[2] = name
#personalInfo[3] = name
personalInfo = ["name","name","year","Contact Number"]




def clicked(*args):
    personalInfo[0] = str(a1.get())
    print(personalInfo[0])
    personalInfo[1] = str(b1.get())
    personalInfo[2] = str(c1.get())
    personalInfo[3] = str(d1.get())
    f = open("data.txt","w")
    f.write("Name: " + personalInfo[0] +" "+ personalInfo[1])
    f.write("\nYear: " + personalInfo[2])
    f.write("\nContact Number: "+ personalInfo[3])
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
# Gets the requested values of the height and widht.
windowWidth = window.winfo_reqwidth()
windowHeight = window.winfo_reqheight()
print("Width",windowWidth,"Height",windowHeight)

# Gets both half the screen width/height and window width/height
positionRight = int(window.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(window.winfo_screenheight()/2 - windowHeight/2)

# Positions the window in the center of the page.
window.geometry("+{}+{}".format(positionRight, positionDown))


window.mainloop()
# if btn == clicked :
#     f = open("data.txt","w")
#     f.write("Name: " + a1 + b1)
#     f.write("Email: " + c1)
#     f.write("Contact Number: "+ d1)
#     f.close()

window.mainloop()

