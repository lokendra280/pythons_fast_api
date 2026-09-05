# def shout(text):
#     return text.upper() + "!"   

# def whisper(text):
#     return text.lower() + "..."


# # higher order function
# def greet(func):
#     greeting = func("Hello, World")
#     print(greeting)


# greet(shout)  # Output: HELLO, WORLD!
# greet(whisper)  # Output: hello, world...
# greet(lambda text: text[::-1])  # Output: dlroW ,olleH


def first_child():
    return "I am the first child."

def second_child():
    return "I am the second child."


def parent(num):
    if num == 1:
        return first_child
    else:
        return second_child


my_child = parent(2)
print(my_child())  # Output: I am the first child.