
# new decorator defination
def new_decorator(original_function):
    def inner_function():
        print("Added at beginning of existing function")
        original_function()
        print("Added at the end of existing function")
    return wrap_function

@new_decorator  # it passed hello as arg to new_decorator
def hello():
    print("Orignal function")
    
hello()

"""
o/p:

Added at beginning of existing function
Orignal function
Added at the end of existing function

instead of @ operator 
the decorator can be called as a function call as well

def new_decorator(original_function):
    def inner_function():
        print("Added at beginning of existing function")
        original_function()
        print("Added at the end of existing function")
    return wrap_function

def hello():
    print("Orignal function")
    
dec_call = new_decorator(hello) # decorator is called passing hello as argument
print(dec_call())

"""
