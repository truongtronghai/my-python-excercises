# You can mix data types in a Python list.
# In other languages, this capability is not a feature of lists :D
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
print(myMixedTypeList)
for i in myMixedTypeList:
    print("{} is an {}".format(i, type(i)))
