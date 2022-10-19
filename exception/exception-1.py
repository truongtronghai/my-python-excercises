
mixedList = ["a",0,2]

for i in mixedList:
    try:
            print("the entry is %s" % i)
            r = 1/i
            print("Rate is ", r)
    except Exception as e:
            print("Oops!", e.__class__, "occurred")
            print("Next entry.")
            print("===============")