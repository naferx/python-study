
class Person:
    
    def __str__(self) -> str:
        return 'Person'


class Client(Person):

    def __init__(self, name) -> None:
        self.name = name
    
    def __str__(self) -> str:
        return f'Client:{self.name} -> ' + super().__str__()


cl = Client('Julia')
print(cl) # Client:Julia -> Person