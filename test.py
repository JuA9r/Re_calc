class Integer:
    def __init__(self):
        self._value = 0

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError("Value must be an integer.")
        self._value = value


class MyClass:
    number = Integer()


# 使用例
if __name__ == "__main__":
    obj = MyClass()

    obj.number = 10
    print(obj.number)

    try:
        obj.number = "Hello"
    except ValueError as e:
        print(e)
