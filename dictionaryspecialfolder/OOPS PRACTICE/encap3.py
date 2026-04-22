class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    def get_fahrenheit(self):
        return (self.__celsius * 9/5) + 32

t = Temperature(25)
print(t.get_fahrenheit())  # 77.0