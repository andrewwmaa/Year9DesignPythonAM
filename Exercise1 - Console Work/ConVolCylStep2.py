import math
print("Volume of a Cylinder Formula: ")
print("V = pi * radius *radius * height")
print("You will need the radius and height")
print("to calculate the volume.") 
#Input
#What inputs are needed to calculate the volume of a cylinder?
name = input("What is your name: ")   #takes users name
if name == "Creeper":
	print ("AW MAN.....")
radius = input("Input radius(cm): ")  #input
radius = float(radius)     #cast to int

height = input("Input height(cm): ") #input
height = float(height)     #cast to int
#Process
#What formula is used to calculate the volume of a cylinder?
volume = math.pi*radius*radius*height
volume = round(volume,2)
#Output
#What is important about the output?
print ("Hi, "+name+")
print ("Cylinder Information:")
print ("Radius = " +str(radius))
print ("Height = " +str(height))
print ("Volume = "+str(volume)+"\n")
