mixedList = ["a",0,-2,4]

for i in mixedList:
    print("the entry is %s" % i)
    
    try: 
        if(type(i)==int and i<0):
            raise ValueError("The entry number is negative") # raise exception manually

        r = 1/i
        print("Rate is ", r)

    except ZeroDivisionError:
        print("Oops! Cannot divide 0")
    except (ValueError,TypeError) as e:
        print("Oops! type or value error occurred")
        print(e)
    except Exception as e:
        # catch all other exceptions
        print("Oops!", e.__class__, "occurred")
        print("Next entry.")
    
    print("===============")