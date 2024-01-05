class Example:
    counter = 0

    def __init__(self, val = 1) -> None:
        self.__first = val
        Example.counter += 1
    

example_object_1 = Example()
example_object_2 = Example(2)
example_object_3 = Example(4)


print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)