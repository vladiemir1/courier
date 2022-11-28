import math
class Couriers:
    def __init__(self, name, x, y, capacity):                   # класс курьера с именем, координатами и грузоподьемностью
        self.name = name
        self.x = x
        self.y = y
        self.capacity = capacity
    def get_dist(self,other_point):
        return math.dist((self.x,self.y),(other_point.x,other_point.y))
