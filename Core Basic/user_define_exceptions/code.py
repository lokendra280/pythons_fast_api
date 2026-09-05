# class CustomError(Exception):
#     """Base class for custom exceptions."""
#     pass

# try:
#     ...
# except CustomError:
#     ...


class InvalideAgeException(Exception):
    pass

try:
    user_age = int(input("Enter your age: "))
    if user_age < 18:
        raise InvalideAgeException()

    else:
        print("You are eligible to vote.")
except InvalideAgeException:
    print("You are not eligible to vote. Age must be 18 or older.")