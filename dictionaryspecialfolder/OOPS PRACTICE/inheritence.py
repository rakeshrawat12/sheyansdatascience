class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):   # Dog inherits Animal
    pass

d = Dog()
d.speak()