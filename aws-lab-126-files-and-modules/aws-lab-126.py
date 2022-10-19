import jsonFile 

filename = "insulin.json";
insulinData =  jsonFile.readJsonFile(filename);

try:
    
    if(insulinData == False):
        raise IOError
    elif insulinData == "":
        print("Cannot read data from file", filename)
    else:
        molecularWeightInsulinActual = insulinData["molecularWeightInsulinActual"]
        aInsulin = insulinData["molecules"]["aInsulin"]
        bInsulin = insulinData["molecules"]["bInsulin"]
        insulin = bInsulin + aInsulin
        
        insulinUppercase = insulin.upper()
        #print("aInsulin",aInsulin)
        #print("bInsulin",bInsulin)
        #print(molecularWeightInsulinActual)

        acidAminWeights = insulinData["weights"]
        # creating a Dictionary of Acid Amin in the Insulin from file with value which is counted in the Insulin string
        acidAminCountsOfInsulin = { aa: insulinUppercase.count(aa)  for aa in ['A','C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T','V', 'W', 'Y']}
        # Multiply the count by the weights
        countMultiplyWeightDict = {aa: acidAminWeights[aa]*acidAminCountsOfInsulin[aa] for aa in ['A','C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T','V', 'W', 'Y']}
        molecularWeightInsulin = sum(countMultiplyWeightDict.values())

        print("The rough molecular weight of insulin: {}".format(molecularWeightInsulin))
        print("Percentage of error: {} %".format(
                    (molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual*100
                ))
        
except IOError:
    print("File is not existed.")
