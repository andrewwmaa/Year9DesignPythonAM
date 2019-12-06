from tkinter import *
import webbrowser

window = Tk()
link = Label(window, text="google.com", fg="blue", cursor="hand2")
link.pack()
link.bind("<Button-1>", lambda event: webbrowser.open(link.cget("text")))
window.mainloop()