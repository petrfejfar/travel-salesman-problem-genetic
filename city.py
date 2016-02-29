from math import sqrt


class City:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

    def __repr__(self):
        return "City %s" % self.name

    def distance(a, b):
        dx = a.x - b.x
        dy = a.y - b.y

        return sqrt(dx*dx+dy*dy)
