#If you don't know Python, 
#DON'T TOUCH THIS CODE.

#Program will take two integers 
#and multiply them

#Input
name = input("Please input your name: ")
a = input("Please input the first number: ")
a = int(a)
b = input("Please input the second number: ")
b = int(b)

#Process
product = a * b

#You can also do this:
#product = float(a) * float(b)

#Output
print(name + ", here is the answer:")
print("The product of " + str(a) + " and " + str(b) +" is " + str(product))