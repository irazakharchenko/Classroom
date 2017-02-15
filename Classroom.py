class Classroom:
    def __init__(self, number, capacity, equipment):
        self.assig(number, capacity, equipment)

    def assig(self, num, cap, equip):
        self.number = num
        self.capacity = int(cap)
        self.equipment = equip

    def is_larger(self, other):
        return self.capacity > other.capacity

    def equipment_differences(self, other):
        return list(set(self.equipment) - set(other.equipment))

    def  __str__ (self):
        strich =  'Classroom {0} has a capacity of {1}  persons and has the following equipment: '\
            .format(self.number, self.capacity)
        for i in self.equipment:
            strich += i + ', '
        return strich[:-2] + '.\n'
    def  __repr__ (self):
        pass



#some comments
cl1 = Classroom('6', 6, ['dsd','ddd'])
cl2 = Classroom('8', 4, [6,7])
print(cl1.__str__())
