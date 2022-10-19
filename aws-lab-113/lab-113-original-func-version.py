import csv
# import copy
# print nicely
#from pprint import pprint

def buildVehicle(lstData):
    myVehicle = {
        "vin" : lstData[0],
        "make" : lstData[1] ,
        "model" : lstData[2] ,
        "year" : lstData[3],
        "range" : lstData[4],
        "topSpeed" : lstData[5],
        "zeroSixty" : lstData[6],
        "mileage" : lstData[7]
    }

    return myVehicle
    

myInventoryList = []

with open('car_fleet.csv') as csvFile:
    
    csvReader = csv.reader(csvFile, delimiter=',')  

    lineCount = 0  

    for row in csvReader:

        if lineCount == 0:
            print("Column names are: {}".format(", ".join(row)))  
        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            
            temporaryDict = buildVehicle(row)
            
            myInventoryList.append(temporaryDict)  

        lineCount += 1  

    print(f'Processed {lineCount} lines.')


print(myInventoryList)

#pprint(myInventoryList)
