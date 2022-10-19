# Python3
# Coding: utf-8  
# Store the human preproinsulin sequence in a variable called preproinsulin:  
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  
# Store the remaining sequence elements of human insulin in variables:  
lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  
insulin = bInsulin + aInsulin

aminoAcids = ["y","c","k","h","r","d","e"]

pKR = {
        "y": 10.07,
        "c": 8.18,
        "k": 10.53,
        "h": 6.00,
        "r": 12.48,
        "d": 3.65,
        "e": 4.25
    }
# creating seqCount with Dict comprehension
seqCount = { i : float(insulin.count(i)) for i in aminoAcids }

pH = 0
while (pH < 14):
    netCharge = (
        sum({ x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) for x in ['k','h','r'] }.values())
        -sum({ x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) for x in ['y','c','d','e'] }.values())
    )

    print("{0}".format(pH), netCharge)
    pH += 1
