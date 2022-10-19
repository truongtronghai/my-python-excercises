import sys
mixedList = ["a",0,2]

for i in mixedList:
    try:
            print("the entry is %s" % i)
            r = 1/i
            print("Rate is ", r)
    except:
            print("Oops!", sys.exc_info()[0], "occurred")
            print("Next entry.")
            print("===============")