"""
create list of odd number in numbers from 2 to 250
"""

odd_numbers = [ x  for x in range(2,251) if x%2!=0 ]
prime_numbers = []

for x in odd_numbers:
        IS_PRIME_NUMBER =True
        for i in range(2,x):
                if x%i==0 :
                        IS_PRIME_NUMBER = False
                        break
        if IS_PRIME_NUMBER:
                prime_numbers.append(x)

with open("results.txt","w") as fh:
        fh.write("Prime numbers between 1 and 250 are: ")
        fh.write(", ".join([ str(x) for x in prime_numbers]))