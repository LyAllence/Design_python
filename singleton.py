# coding:utf8


class Singleton(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'one'):
            org = super(Singleton, cls)
            cls.one = org.__new__(cls)
        return cls.one


if __name__ == '__main__':
    class SingleSpam(Singleton):
        def __init__(self, s):
            self.s = s

        def __str__(self):
            return self.s


    s1 = SingleSpam('spam')
    print(id(s1), s1)
    s2 = SingleSpam('spa')
    print(id(s2), s2)
    print(id(s1), s1)
