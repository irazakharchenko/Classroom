class Classroom:
    def __init__(self, number, capacity, equipment):
        self.assig(number, capacity, equipment)

    def assig(self, num, cap, equip):
        self.number = num
        self.capacity = int(cap)
        self.equipment = equip

    def is_larger(self, other):
        return self.capacity > other.capacity

cl1 = Classroom('6', 6, [7,8])
cl2 = Classroom('8', 4, [6,7])
print(cl1.is_larger(cl2))
