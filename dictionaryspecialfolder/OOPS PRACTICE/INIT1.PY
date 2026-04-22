class Dataset:
    def __init__(self, name, rows):
        self.name = name
        self.rows = rows

    def show(self):
        print(f"Dataset: {self.name}, Rows: {self.rows}")

d1 = Dataset("Iris", 150)
d1.show()