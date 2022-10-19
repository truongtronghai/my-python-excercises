def cong(a, b):
    d = a+b
    return d

def substract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    if b==0:
       return False
    
    return a/b

def soNguyenTo(n):
    for i in range(2,n):
        if (n%i)==0 :
            return False

    return True

"""
numb = int(input("Nhap vao mot so: "))

if ( numb<=1 ) :
    print("So can nhap vao phai lon hon 1")
else:
    if soNguyenTo(numb):
        print("{} la so NGUYEN TO".format(numb))
    else:
        print("{} khong phai la so NGUYEN TO".format(numb))
"""
"""
n1 = int(input("Tu: "))
n2 = int(input("Den: "))

for i in range(n1,n2+1):
    if soNguyenTo(i):
        print(i)

print("=================================================")
"""

import json

person = '{"name": "Bob","languages": ["English","French"]}'

person_dict = json.loads(person)

#print(person_dict)

#print(person_dict["languages"])

with open("sample.json","r") as fh:
    data = json.load(fh)

#print(data)


person_dict = {
        "name": "Bob",
        "age": 12,
        "children": None
    }

person_json = json.dumps(person_dict) # return a string of JSON

print(type(person_json))
print(person_json)
