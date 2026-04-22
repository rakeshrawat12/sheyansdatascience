class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks

    def get_marks(self):
        return self.__marks

s = Student("Ravi", 80)
s.set_marks(90)
print(s.get_marks())