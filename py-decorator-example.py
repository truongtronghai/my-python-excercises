def make_pretty(func):
    def inner(x):
        print("I got decorated")
        func(x)
    return inner

def general_pretty(func):
    def wrapper(*args, **kwargs):
        print("Starting wrapper")
        print(func(*args, **kwargs))
        print("Ending wrapper")
        
    return wrapper

@make_pretty
def ordinary(ten):
    print(ten + " I am ordinary")


@general_pretty
def super_ordinary(ten):
    print(ten + " I am super ordinary")

    
# ordinary("Nguyen")
# super_ordinary("Nguyen")

@general_pretty
def add(a,b):
    return a+b


add(4,5)
