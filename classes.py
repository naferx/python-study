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
   

st = MyStack()
st.push(2)
st.push(6)
print(st.pop())