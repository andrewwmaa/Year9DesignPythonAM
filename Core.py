import tkinter as tk
import datetime as dt
from tkinter import *
from tkinter import ttk
print("Start Program.")

root = tk.Tk() #builds main window

#widget/element is an element in a GUI
#button, text box, input box, slider, dropdown, image, video, etc.

#1: Construct the widget
txt1 = tk.Label(root, width = 30, height = 30)

#date = (os.system("date"))

#2: Config
txt1.config(text = "It is")
#btn2.config(text = date)

#3: Packing it
txt1.pack()
#btn2.pack()

w = tk.Label(root, text=f"{dt.datetime.now():%a, %b %d %Y}")
w.pack()


output = tk.Text(root, width = 100, height = 20)
output.config()
output.pack()
root.mainloop()
print("End Program.")

