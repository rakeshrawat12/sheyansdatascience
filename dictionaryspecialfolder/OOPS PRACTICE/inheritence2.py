class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    pass

d = Dog("Tommy")
print(d.name)