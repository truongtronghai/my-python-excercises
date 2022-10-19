def add(num1: int, num2: int):
    num3= num1 + num2
    return num3

def sub(num1: int, num2: int):  
    num3= num1 - num2
    return num3

def mul(num1: int, num2: int):  
    num3= num1 * num2
    return num3

def div(num1: int, num2: int):  
    num3 = num1/ num2
    return num3  




print('Nhap num1')
num1 = int(input())

print('Nhap num2')
num2 = int(input(num2)) 

while num2 ==0:
    print('Nhap lai num2 khac 0') 
    num2 = int(input(num2)) 

a =add(num1+num2)
print(f'Tong cua {num1} va {num2} la:{a}')

b =sub(num1,num2)
print(f'Hieu cua {num1} va {num2} la:{b}')

c =mul(num1,num2)
print(f'Tich cua {num1} va {num2} la:{c}')

d =div(num1,num2)
print(f'Tich cua {num1} va {num2} la:{d}')