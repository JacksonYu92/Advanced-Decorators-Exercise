# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        function()
        print(f"You called {function.__name__}{args}\nIt returned: {function(*args)}")
    return wrapper


# Use the decorator 👇
@logging_decorator
def a_function(*args):
    result = 1
    for n in args:
        result *= n
    return result

a_function(1,2,3)