class TestClass:
    pass

obj = TestClass()

class MyStack:
    def __init__(self) -> None:
        self.__stack = []

    def push(self, value) -> None:
        self.__stack.append(value)

    def pop(self):
        val = self.__stack[-1]
        del self.__stack[-1]
        return val

class AddingStack(MyStack):   
    def __init__(self) -> None:
        MyStack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum
    
    def pop(self):
        v = MyStack.pop(self)
        self.__sum -= v
        return v
    
    def push(self, v):
        MyStack.push(self, v)
        self.__sum += v


st = AddingStack()
st.push(2)
st.push(6)
print(st.get_sum())