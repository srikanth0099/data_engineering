# Create a decorator that logs the name of the function which is being called, the arguments passed and return value of the function

import functools

def log_function_name(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Name of Calling function: {function.__name__}")
        print(f"Arguments passed: args={args}, kwargs={kwargs}")
        output = function(*args, **kwargs)
        print(f"Return value: {output}")
        return output
    return wrapper

@log_function_name
def multiply(a, b):
    return a * b

output = multiply(7, 9)


