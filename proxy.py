# coding:utf8

import time


class SalesManager:
    @staticmethod
    def work():
        print("Sales Manager working...")

    @staticmethod
    def talk():
        print("Sales Manager ready to talk")


class Proxy:
    def __init__(self):
        self.busy = 'No'
        self.sales = None

    def work(self):
        print("Proxy checking for Sales Manager availability")
        if self.busy == 'No':
            self.sales = SalesManager()
            time.sleep(2)
            self.sales.talk()
        else:
            time.sleep(2)
            print("Sales Manager is busy")


if __name__ == '__main__':
    p = Proxy()
    p.work()
    p.busy = 'Yes'
    p.work()
