# coding:utf8


class AbstractExpression:
    def interpret(self):
        pass


class Expression(AbstractExpression):
    def interpret(self):
        print("terminal interpret")


class NoExpression(AbstractExpression):
    def interpret(self):
        print("Non terminal interpret")


if __name__ == "__main__":
    c = []
    c.extend([Expression()])
    c.extend([NoExpression()])
    c.extend([Expression()])
    c.extend([Expression()])
    for a in c:
        a.interpret()
