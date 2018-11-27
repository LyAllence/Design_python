# coding: utf-8


class Person(object):

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return 'people name is {}'.format(self.name)


class Animal(object):

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return 'animal name is {0}'.format(self.name)


def create_name(kind='person'):
    if kind == 'person':
        return Person
    elif kind == 'animal':
        return Animal


if __name__ == '__main__':
    p, a = create_name()('alice'), create_name('animal')('ben')
    print(p.get_name())
    print(a.get_name())
