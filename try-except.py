def divide_five_by(num):
    try:
        value = 5/num
    except ZeroDivisionError:
        print('Divide by zero error')
        value = 1
    else:
        print("No error catched!")
    finally:
        print("No matter what")
        
    return value

print(divide_five_by(2))
print("==========")
print(divide_five_by(0))
