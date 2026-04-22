class DataAnalysis:
    def __init__(self, data):
        self.data = data

    def mean(self):
        return sum(self.data) / len(self.data)

d = DataAnalysis([10, 20, 30, 40])
print("Mean:", d.mean())