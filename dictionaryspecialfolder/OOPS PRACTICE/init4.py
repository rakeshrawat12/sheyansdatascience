class Scaler:
    def __init__(self, data):
        self.data = data

    def min_max_scale(self):
        min_val = min(self.data)
        max_val = max(self.data)

        scaled = [(x - min_val) / (max_val - min_val) for x in self.data]
        return scaled

d = Scaler([10, 20, 30, 40])
print("Scaled Data:", d.min_max_scale())