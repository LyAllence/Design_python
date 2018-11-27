# coding:utf8


class Component:

    def __init__(self, name):
        self.name = name

    def add(self, com):
        pass

    def display(self, depth):
        pass


class Leaf(Component):
    def add(self, com):
        print("leaf can't add")

    def display(self, depth):
        temp = "-" * depth
        temp = temp+self.name
        print(temp)


class Composite(Component):

    def __init__(self, name):
        super().__init__(name)
        self.c = []

    def add(self, com):
        self.c.append(com)

    def display(self, depth):
        temp = "-" * depth
        temp = temp+self.name
        print(temp)
        for com in self.c:
            com.display(depth + 2)


if __name__ == "__main__":
    p = Composite("Wong")
    p.add(Leaf("Lee"))
    p.add(Leaf("Zao"))
    p1 = Composite("Wu")
    p1.add(Leaf("San"))
    p.add(p1)
    p.display(1)
