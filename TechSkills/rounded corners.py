from tkinter import *

root = Tk()
canvas = Canvas(width = 400, height = 400, bg = "snow")
canvas.pack()
canvas.create_rectangle(100,100,300,250)
#canvas.create_text(100,10,fill="black",font="Helvetica 20 italic bold", text="Click the bubbles that are multiples of two.")
text = Text(canvas).pack()
#text = Entry(canvas).pack()
root.mainloop()