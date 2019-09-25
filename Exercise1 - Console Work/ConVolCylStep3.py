import math


print("\n\tVolume of a Cylinder formula:")
print("\n\t\t\tV = \u03C0 \u00D7 radius\u00B2 \u00D7 height")
print("\n\tThis program will take as input the radius and height")
print("\tand print the volume.")

#Input
#What inputs are needed to calculate the volume of a cylinder?
name = input("\n\tWhat is your name: ")
if name == "Creeper":
	print ("\n\tAW MAN.....")
radius = 1
height = 1

while (radius != 0 or height != 0):

	radius = input("\n\tInput radius (cm): ")
	radius = int(radius)

	height = input("\n\tInput height (cm): ")
	height = int(height)
	#Process
	#What formula is used to calculate the volume of a cylinder?
	#V = pi * r * r * h

	if (radius >= 0 and height >= 0):

		volume = math.pi * radius * radius * height
		volume = round(volume,2)
		#Output
		#What is important about the output?
		print("\n\t\tHi "+name+"!")
		print("\n\t\tGive a cylinder with:")
		print("\t\tRadius = "+str(radius))
		print("\t\tHeight = "+str(height))
		print("\t\tThe volume is: "+str(volume)+"\n")
	else:
		print("\n\t\tYou have entered an invalid value")
	#Checks while boolean expression

print("Thank You. The Program has been completed.")
