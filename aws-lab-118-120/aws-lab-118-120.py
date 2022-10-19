from pprint import pprint

# Store the human preproinsulin sequence in a variable called preproinsulin:
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
# Store the remaining sequence elements of human insulin in variables:
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

insulin = bInsulin + aInsulin

# Printing "the sequence of human insulin" to console using successive print() commands:
print("The sequence of human preproinsulin: %s" % preproInsulin)
# Printing to console using concatenated strings inside the print function (one-liner):
print("The sequence of human insulin, chain a: " + aInsulin)
print("The sequence of human insulin, chain b: ", bInsulin)
print("The sequence of human insulin, chain c: " + cInsulin)

# Calculating the molecular weight of insulin  
# Creating a dictionary of the amino acid (AA) weights  
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19}  

# Count the number of each amino acids
# The count() method returns the number of times a specified value appears in the string.
# aaCountInsulin = {x: float(insulin.upper().count(x)) for x in ['A', 'C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T','V', 'W', 'Y']}  
"""
I rewrited aaCountInsulin variable for reading easiler than the original code. In the origin, the writer uses Dictionary Comprehension to create new Dictionary.
That is really a bullshit to use for guiding a brand new Python programmer!!!
"""
aaCountInsulin = {}
insulinUpper = insulin.upper()
for x in ['A', 'C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T','V', 'W', 'Y']:
	aaCountInsulin[x] = float(insulinUpper.count(x))
	
# Multiply the count by the weights  
#molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T', 'V', 'W', 'Y']}.values())
#print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))
"""
I rewrited molecularWeightInsulin variable for reading easiler than the original code
"""
molecularWeightInsulinDict = {}
for x in ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T', 'V', 'W', 'Y']:
	molecularWeightInsulinDict[x] = aaCountInsulin[x] * aaWeights[x]

"""
#The values() method returns the values of the dictionary, as a LIST.

#The sum() function returns a number, the sum of all items in an iterable.
Syntax: sum(iterable, start)

	Parameter	Description
	iterable	Required. The sequence to sum
	start	Optional. A value that is added to the return value
	
"""
tempList = molecularWeightInsulinDict.values()
molecularWeightInsulin = sum(tempList)
print("The rough molecular weight of insulin: ", molecularWeightInsulin)

molecularWeightInsulinActual = 5807.63

percentageErrorInsulin = ((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100

print("Error percentage: {} %".format(str(percentageErrorInsulin)))
