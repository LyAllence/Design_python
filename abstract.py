#!/usr/bin/python
#coding:utf8


class Dog(object):

    def __init__(self):
        self.name = 'dog'

    def print_food(self):
        print(self.name)
        return 'dog food'


class Cat(object):

    def __init__(self):
        self.name = 'cat'

    def print_food(self):
        print(self.name)
        return 'cat food'


class Factory(object):

    def __init__(self, auto_class=None):
        self.auto_class = auto_class

    def print_food(self):
        return self.auto_class.print_food()


if __name__ == '__main__':
    d = Dog()
    c = Cat()
    f = Factory()
    f.auto_class = d
    print(f.print_food())
    f.auto_class = c
    print(f.print_food())

