#!/usr/bin/python
# coding:utf8


class Dog(object):
    def __init__(self):
        self.name = "Dog"

    @staticmethod
    def bark():
        return "woof!"


class Cat(object):
    def __init__(self):
        self.name = "Cat"

    @staticmethod
    def meow():
        return "meow!"


class Human(object):
    def __init__(self):
        self.name = "Human"

    @staticmethod
    def speak():
        return "'hello'"


class Car(object):
    def __init__(self):
        self.name = "Car"

    @staticmethod
    def make_noise(octane_level):
        return "room %s" % ("!" * octane_level)


class Adapter(object):
    """
    Adapts an object by replacing methods.
    Usage:
    dog = Dog
    dog = Adapter(dog, dict(make_noise=dog.bark))
    """
    def __init__(self, obj, adapted_methods):
        """We set the adapted methods in the object's dict"""
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object"""
        return getattr(self.obj, attr)


def main():
    objects = []
    dog = Dog()
    objects.append(Adapter(dog, dict(make_noise=dog.bark)))
    cat = Cat()
    objects.append(Adapter(cat, dict(make_noise=cat.meow)))
    human = Human()
    objects.append(Adapter(human, dict(make_noise=human.speak)))
    car = Car()
    objects.append(Adapter(car, dict(make_noise=lambda: car.make_noise(3))))

    for obj in objects:
        print("A", obj.name, "goes", obj.make_noise())


if __name__ == "__main__":
    main()
