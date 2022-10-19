import logging
logging.basicConfig(filename="app.log", filemode='w', level=logging.DEBUG)
'''
# logging
def checkValueLogging(valuetocheck):
    if (type(valuetocheck) is not int):
        print("You must enter a number.")
        logging.debug("User input a non-numeric value")
    elif (valuetocheck <= 0):
        print("Value entered must be greater than 0")
        logging.warning("Value entered must be greater than 0")  
    elif (valuetocheck > 4):
        print("Value is greater than 4")
        logging.info("User supplied value greater than 4")
    else:
        print("You just input %s" % (valuetocheck))
        logging.info("User typed %s" % (valuetocheck))

try:
    var = int(input("Enter a number greater than 0:"))
    checkValueLogging(var);
except ValueError as err:
    logging.error(err)
else:    
    print("End program!")

'''
# assert keyword
def checkValueUsingAssert(valuetocheck):
    assert (type(valuetocheck) is int), "You must enter a number."
    assert (valuetocheck > 0), "Value entered must be greater than 0"
    if valuetocheck > 4:
        print("Value is greater than 4")
    else:
        print("Value is less than 4")

var = int(input("Enter a number greater than 0:"))

try:
    checkValueUsingAssert(var)
except AssertionError as err:
    print(err)
