import random


def __test_decorator__(func):
    def wrapper(*args, **kwargs):
        print("Running")
        result = func(*args, **kwargs)
        print("finished")
        print("-"*20)
        return result
    return wrapper


@__test_decorator__
def test(a, b):
    return a + b

print("\n",f"result: {test(random.randint(1, 100), random.randint(1, 100))}")
