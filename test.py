import random


def __test_decorator__(func):
    def wrapper(*args, **kwargs):
        print("Running")
        result = func(*args, **kwargs)
        print("finished")
        print("-"*20, "\n")
        return result
    return wrapper


@__test_decorator__
def __test__(a, b):
    return a + b


print(f"result: {__test__(random.randint(1, 100), random.randint(1, 100))}")