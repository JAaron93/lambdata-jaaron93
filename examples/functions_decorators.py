"""Examples of weird function things and decorators"""

def say_hello(name):
    return f"Hello {name}"

def be_cool(name):
    return f"Yo {name}, together we are cool!"

def greet_bob(say_hello):
    return greeter_func("Bob")

if __name__ == "__main__":
    greet_bob(say_hello)
    greet_bob(be_cool)

def mess_with_list(some_list):
    return some_list.lower()

# Functions inside functions
def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

# What a decorator essentially does
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is online")
        func()
        print("Something is happening after the function is called")

    return wrapper

def say_whee():
    print("Wheee!")


# What a decorator does
say_whee = my_decorator(say_whee)


# Decorator syntax
@my_decorator
def say_whee_2():
    print("Whee!")


say_whee_2()
