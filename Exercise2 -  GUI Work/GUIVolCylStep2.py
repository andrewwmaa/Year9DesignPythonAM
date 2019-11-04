import math
import tkinter as tk
import tkinter.font as tkfont
#Main Code:
root = tk.Tk()
title = tk.Label(root, text = "Cylinder Volume Calculator")
helv36 = tkfont.Font(family = "Helvetica Neue",size = 36, weight = "bold")
radiusLabel = tk.Label(root, text = "Radius:")
radiusEntry = tk.Entry(root)
heightLabel = tk.Label(root, text = "Height:")
heightEntry = tk.Entry(root)
btnrun = tk.Button(root, text = "CALCULATE", highlightbackground='white')
check = tk.Checkbutton(root, text = "High Contrast")

output = tk.Text(root)


#config
title.config(fg = "black", bg = "white")
radiusLabel.config(anchor = tk.W)
radiusEntry.config()
heightEntry.config()
heightLabel.config(anchor = tk.W)
btnrun.config(fg="black")
check.config(anchor = tk.W)

output.config(width = 50, height = 10, state = "disabled", borderwidth = 2, relief = "groove")

#pack
title.pack(fill = tk.BOTH)
radiusLabel.pack(fill = tk.BOTH)
radiusEntry.pack(fill = tk.BOTH)
heightLabel.pack(fill = tk.BOTH)
heightEntry.pack(fill = tk.BOTH)
btnrun.pack(fill = tk.BOTH)
check.pack(fill = tk.BOTH)
output.pack()

#Building widgets goes before mainloop.
root.mainloop()
print("End Program")

def calcVolCylinder():

	print("\n\tVolume of a Cylinder formula:")
	print("\n\t\t\tV = \u03C0 \u00D7 radius\u00B2 \u00D7 height")
	print("\n\tThis program will take as input the radius and height")
	print("\tand print the volume.")

	file = open("data.txt","a") #w,r,a

	name = input("\n\tWhat is your name: ")
	if name == "Creeper":
		print ("\n\tAW MAN.....")
	radius = 0
	height = 0

	try:
		radius = input("\n\tInput radius (cm): ")
		radius = int(radius)

		height = input("\n\tInput height (cm): ")
		height = int(height)
	except:
		print("\n\t\tNumeric Type Required")
		height = -1
		radius = -1

	if (radius >= 0 and height >= 0):

		volume = math.pi * radius * radius * height
		volume = round(volume,2)
		print("\n\t\tHi "+name+"!")
		print("\n\t\tGive a cylinder with:")
		print("\t\tRadius = "+str(radius))
		print("\t\tHeight = "+str(height))
		print("\t\tThe volume is: "+str(volume)+"\n")
		file.write(str(volume)+"\n")
	else:
		print("\n\t\tYou have entered an invalid value.")


	print("Thank You. The Program has been completed.")
	file.close()
