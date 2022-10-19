'''
Python try with else clause

In some situations, you might want to run a certain block of code if the code block inside try ran without any errors.
For these cases, you can use the optional else keyword with the try statement.
'''
mixedList = [1,2,4,0]

for i in mixedList:
    try:
        print("Entry number: ",i)
        assert i%2 == 0 # if not equal, this raise an exception
    except:
        print("This entry is an odd number")
    else:
        print("This entry is an even number")
        r = 1/i
        print("Rate: ",r)

    print()