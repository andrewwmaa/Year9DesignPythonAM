import math
print("\n\tVolume of a Cylinder Formula:")
print("\n\t\t\tV = \u03C0\u00d7radius\u00b2\u00d7height")
print("\n\tThis program will take as input the radius and height")
print("\tand print the volume.")
#Input
#What inputs are needed to calculate the volume of a cylinder?
name = input("\n\tWhat is your name: ")   #takes users name
if name == "Creeper":
	print ("AW MAN.....")
radius = input("\n\tInput radius(cm): ")  #input
radius = float(radius)     #cast to int

height = input("\n\tInput height(cm): ") #input
height = float(height)     #cast to int
#Process
#What formula is used to calculate the volume of a cylinder?
volume = math.pi*radius*radius*height
volume = round(volume,2)
#Output
#What is important about the output?
print ("\n\tHi "+name+"!")
print ("\n\tCylinder Information:")
print ("\n\tRadius = " +str(radius))
print ("\n\tHeight = " +str(height))
print ("\n\tVolume = "+str(volume)+"\n")
