import tkinter as tk
from PyQt4 import QtGui    # or PySide

def center(toplevel):
    toplevel.update_idletasks()

    # Tkinter way to find the screen resolution
    # screen_width = toplevel.winfo_screenwidth()
    # screen_height = toplevel.winfo_screenheight()

    # PyQt way to find the screen resolution
    app = QtGui.QApplication([])
    screen_width = app.desktop().screenGeometry().width()
    screen_height = app.desktop().screenGeometry().height()

    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = screen_width/2 - size[0]/2
    y = screen_height/2 - size[1]/2

    toplevel.geometry("+%d+%d" % (x, y))
    toplevel.title("Centered!")    

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Not centered")

    win = tk.Toplevel(root)
    center(win)

    root.mainloop()