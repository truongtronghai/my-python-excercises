mixedList = ["a",0,2]

for i in mixedList:
    print("the entry is %s" % i)
    try: 
        r = 1/i
        print("Rate is ", r)
    except ZeroDivisionError:
        print("Oops! Cannot divide 0")
    except (ValueError,TypeError):
        print("Oops! type or value error occurred")
    except Exception as e:
        # catch all other exceptions
        print("Oops!", e.__class__, "occurred")
        print("Next entry.")
    
    print("===============")