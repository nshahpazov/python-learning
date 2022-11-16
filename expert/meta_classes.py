def f(self):
    print("Hello there")


class MetaBase(type):
    def __new__(cls, name, bases, body):
        # print("BaseMEta", cls, name, bases, body)
        body["bar"] = f
        if not "bar" in body and name != "Base":
            raise TypeError("Bad User")
        return super().__new__(cls, name, bases, body)


class Base(metaclass=MetaBase):
    def foo(self):
        self.bar()


class Base2:
    def foo(self):
        self.bar()

    def __init_subclass__(cls) -> None:
        print("hello from inner class")
        print(cls)
        return super().__init_subclass__()
