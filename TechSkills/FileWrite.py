import tkinter as tk

file = open("sample.txt","a")

file.write(str(hi)+"\n")
file.write(str(how)+"\n")
file.write(str(are u?)+"\n")

file.close()
