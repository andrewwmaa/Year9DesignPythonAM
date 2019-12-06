from tkinter import *
import tkinter 
import numpy as np
import matplotlib.pyplot as plt
import webbrowser
import time


personalInfo = ["name","name","year","Contact Number"]

#when the button "submit" is clicked, it will produce a new window with the graph.
def newWindow():
    #data
    height = [3, 12, 5, 18, 45]
    bars = ('A', 'B', 'C', 'D', 'E')
    y_pos = np.arange(len(bars))
    plt.bar(y_pos, height)
    
    # Create names on the x-axis
    plt.xticks(y_pos, bars)
    plt.show()
  
    
    # Show graphic
 


# when the button is clicked, the data from the labels will be sent to a file named data.txt 
# and is formatted properly
def clicked(*args):
    #gets the label text
    personalInfo[0] = str(a1.get())
    print(personalInfo[0])
    personalInfo[1] = str(b1.get())
    personalInfo[2] = str(c1.get())
    personalInfo[3] = str(d1.get())
    f = open("data.txt","w")
    f.write("Name: " + personalInfo[0] +" "+ personalInfo[1])
    f.write("\nYear: " + personalInfo[2])
    f.write("\nReason: "+ personalInfo[3])
    f.close()


    
    newWindow()



#window names and formatting
window = Tk()
window.title("Submit a Report")
window.geometry('400x400')
window.configure(background = "white");

#time of system styling
time1 = ''
clock = Label(window, font=('arial', 20), bg='white')
clock.grid(row=10,column= 0)

#time function using time module and getting the time from the mac
def tick():
    global time1
    # get the current local time from the mac
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)

tick()

#labels for all the boxes
a = Label(window ,text = "First Name").grid(row = 0,column = 0)
b = Label(window ,text = "Last Name").grid(row = 1,column = 0)
c = Label(window ,text = "Year").grid(row = 2,column = 0)
d = Label(window ,text = "Reason").grid(row = 3,column = 0)

#placement and entry boxes for the labels
a1 = Entry(window)
a1.grid(row = 0,column = 1)

b1 = Entry(window)
b1.grid(row = 1,column = 1)

c1 = Entry(window)
c1.grid(row = 2,column = 1)

d1 = Entry(window)
d1.grid(row = 3,column = 1)

#hyperlinks for easy access
link = Label(window, text="ManageBac", fg="blue", cursor="hand2")
#when hovering over the link and styling of text
link.grid(row = 7,column = 0)
#position
link.bind("<Button-1>", lambda event: webbrowser.open("https://ucc.managebac.com/"))
#actual link and URL of the text

link1 = Label(window, text="MySchoolApp", fg="blue", cursor="hand2")
link1.grid(row = 8,column = 0)
link1.bind("<Button-1>", lambda event: webbrowser.open("https://ucc.myschoolapp.com/app?bb_id=1#"))

link2 = Label(window, text="PowerSchool", fg="blue", cursor="hand2")
link2.grid(row = 9,column = 0)
link2.bind("<Button-1>", lambda event: webbrowser.open("http://ucc.learning.powerschool.com/"))

#submit button
btn = tkinter.Button(window ,text="Submit", command = clicked).grid(row=4,column=0)
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
