class SimpleModel:
    def __init__(self, X, y):
        self.X = X
        self.y = y

    def info(self):
        print("Number of samples:", len(self.X))
        print("Number of labels:", len(self.y))

X = [[1], [2], [3]]
y = [2, 4, 6]

model = SimpleModel(X, y)
model.info()