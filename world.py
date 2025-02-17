class World(object):
    def __init__(self, size=1000, region_count=1):
        self.size = size
        self.region_count = region_count

    def region_for(self, x, y):
        return int(x // self.size)

    def max_x(self):
        return self.region_count * self.size - 1

    @staticmethod
    def min_x():
        return 0

    def in_x_bounds(self, x):
        return self.min_x() <= x <= self.max_x()

    def in_y_bounds(self, y):
        return self.min_y() <= y <= self.max_y()

    @staticmethod
    def min_y():
        return 0

    def max_y(self):
        return self.size - 1
