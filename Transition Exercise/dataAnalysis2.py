print("DATA ANALYSIS 2")
data = open("/Users/andrew.ma/Desktop/git repo/Year9DesignPythonAM/Transition Exercise/randomDataRAW.txt"); 
dataString = data.read()
dataList = dataString.split("\n")

print(dataList)

#Big Skill: Looping through a list using counted loop.  
for i in range(0, len(dataList),1):
	#Big Skill: Removing Elements
	dataList[i] = dataList[i].replace(",","")
	#Big Skill: Casting
	dataList[i] = float(dataList[i])

print(dataList)


#Big Skill: When finding max or min element in list alaways
#			set the max/min to an element in the list

#Find largest
max = dataList[0] #always set

for i in range(0, len(dataList),1):
	if dataList[i] > max:
		max = dataList[i]

print(max)


#Find smallest
#Find mean, median, mode
#Remove outliers (inner quartile range)
