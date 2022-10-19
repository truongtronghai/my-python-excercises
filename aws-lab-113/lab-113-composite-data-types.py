"""
Some notes about Dictionary in Python
Url: https://towardsdatascience.com/15-things-you-should-know-about-dictionaries-in-python-44c55e75405c
NOTES:
* Copy a dictionary
> To copy a dictionary, we can simply use the dict.copy() method. This method returns a shallow copy of the dictionary. We have to be careful with shallow copies, since if your dictionary contains another container-objects like lists, tuples, or sets, they will be referenced again and not duplicated.
> To avoid this problem, we can create a deep copy using copy.deepcopy(x)
> The difference between shallow copies and deep copies is only relevant when the dictionary contains other objects like lists, since those objects will be referenced instead of duplicated (shallow copy). To create a fully independent clone of the original dictionary, we have to make a deep copy.
> If you want to know more about how to copy a dictionary, you can read the following article where the differences between shallow copies and deep copies are explained in detail:
----> https://thispointer.com/python-how-to-copy-a-dictionary-shallow-copy-vs-deep-copy/
> It is important to bear in mind that the = operator does not make a copy of the dictionary. It is just another name to refer to the same dictionary, meaning any modification to the new dictionary is reflected in the original one.
"""

import csv
#import copy

myVehicle = {
        "vin": "<empty>",
        "make": "<empty>",
        "model": "<empty",
        "year": 0,
        "range": 0,
        "topSpeed": 0,
        "zeroSixty": 0.0,
        "mileage": 0
    }

#for key,value in myVehicle.items():
#    print("{} : {}".format(key,value))

myInventoryList = [] # empty list

with open("car_fleet.csv") as fCsv:
    
    lineCount = 0
	
    lines = csv.reader(fCsv,delimiter=",")
	
    for line in lines: # every line in reader object is an List

        #print("{}".format(" , ".join(line)))
        print("%s" % " , ".join(line))
        
        if lineCount != 0 :           
            myVehicle["vin"]=line[0]
            myVehicle["make"]=line[1]
            myVehicle["model"]=line[2]
            myVehicle["year"]=line[3]
            myVehicle["range"]=line[4]
            myVehicle["topSpeed"]=line[5]
            myVehicle["zeroSixty"]=line[6]
            myVehicle["mileage"]=line[7]
            
            myInventoryList.append(myVehicle.copy())
            #print(myInventoryList)
			
        lineCount += 1

    print("Processed {} lines".format(lineCount))
    

print("=====Inventory list========")
for car in myInventoryList:
    for key,value in car.items():
        print("{}: {}".format(key, value))

    print("++++++++")

