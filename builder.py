# coding:utf8


class Thing(object):

    def __init__(self):
        self.building = None

    def set_building(self):
        self.building.new_building()
        self.building.set_floor()
        self.building.set_size()

    def get_building(self):
        return self.building


class Build(object):

    def __init__(self):
        self.building = None

    def new_building(self):
        self.building = Building()


class Building(object):

    def __init__(self):
        self.floor = None
        self.size = None

    def __repr__(self):
        return "floor:" + self.floor + " size:" + self.size


class Cat(Build):

    def set_floor(self):
        self.building.floor = "1"

    def set_size(self):
        self.building.size = 'small'


class Dog(Build):

    def set_floor(self):
        self.building.floor = "2"

    def set_size(self):
        self.building.size = 'big'


if __name__ == '__main__':
    t = Thing()
    t.building = Cat()
    t.set_building()
    print(t.get_building())
    t.building = Dog()
    t.set_building()
    print(t.get_building())
