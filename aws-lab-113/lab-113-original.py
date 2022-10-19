import csv
import copy
#from pprint import pprint

myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

myInventoryList = [] # luu tru ket qua sau khi doc tu file csv

with open('car_fleet.csv') as csvFile:
    
    csvReader = csv.reader(csvFile, delimiter=',')  
    
    lineCount = 0  # khoi tao bien voi gia tri ban dau la 0 de dem so dong doc duoc tu tap tin

    for row in csvReader:

        print(row)
        
        
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            input()
            # currentVehicle = myVehicle
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)  
            lineCount += 1  

    print(f'Processed {lineCount} lines.')
	
#pprint(myInventoryList)
