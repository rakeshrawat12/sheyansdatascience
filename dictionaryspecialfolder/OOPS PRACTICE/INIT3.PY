class DataCleaner:
    def __init__(self, data):
        self.data = data

    def clean(self):
        self.data = [x for x in self.data if x >= 0]
        return self.data

d = DataCleaner([10, -5, 20, -2, 30])
print("Clean Data:", d.clean())