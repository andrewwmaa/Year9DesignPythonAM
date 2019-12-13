print("DATA ANALYSIS 1")
#Beyond the Coding: Files verses Data structures (lists)

#	Files are used to store the data so the data remains when
#	the program isn't running.  A data structure is where the data
#	lives when the program is running.  When using data from files
#	it must be copied into a file.  When the program is done running
#	the information must be copied back into the file.

#Beyond the Coding:  
#	Knowing how the data in your file is organizedis essential.  The 
#	algoritms used to format the data into something that is useable 
#	is based on knowing how it is stored. 

#Big Skill: Reading from text file.
data = open("/Users/andrew.ma/Desktop/git repo/Year9DesignPythonAM/Transition Exercise/randomDataExtract1.txt","r")
dataString = data.read()
dataList = dataString.split("\n")

#Beyond the Coding:  
#	The order of the data could be important
#	if any of the analysis requires changing 
#	the order you need to make a copy of the 
#	information
#
#print(dataList)

#Big Skill: Looping through a list using counted loop.  

#print(dataList)


maximum = max(dataList)
print(maximum)
minimum = min(dataList)
diff = maximum - minimum
smallest = dataList[0]
for i in range(0, len(dataList),1):
	if smallest > dataList[i]:
		smallest = dataList[i]

print("minimum is" + str(smallest))

ctr = 0
for i in range(0, len(dataList), 1):
	if (dataList[i] < 100):
		ctr = ctr+1
		Qprint (dataList[i])

