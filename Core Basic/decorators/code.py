def make_preety(func):
    def inner(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return inner


def ordinary_function():
    print("I am an ordinary function.")

# decorated_function = make_preety(ordinary_function)
# decorated_function()




@make_preety
def decorated_function():
    print("I am a decorated function.")

# ordinary_function()
decorated_function()