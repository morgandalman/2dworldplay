class Region(object):
    def __init__(self, index, size):
        self.size = size
        self.index = index

    def max_x(self):
        return (self.index + 1) * self.size - 1

    def min_x(self):
        return self.index * self.size

    def in_x_bounds(self, x):
        return self.min_x() <= x <= self.max_x()

    def in_y_bounds(self, y):
        return self.min_y() <= y <= self.max_y()

    @staticmethod
    def min_y():
        return 0

    def max_y(self):
        return self.size - 1
