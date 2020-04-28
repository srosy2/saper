# -*- coding: utf-8 -*-
class Model:

    def __init__(self):
        self._A = 0
        self._B = 0
        self._Sum = 0

        self._Observers = []  # список наблюдателей

    @property
    def a(self):
        return self._A

    @property
    def b(self):
        return self._B

    @property
    def sum(self):
        return self._Sum

    @a.setter
    def a(self, value):
        self._A = value
        self._Sum = self._A + self._B
        self.notifyObservers()

    @b.setter
    def b(self, value):
        self._B = value
        self._Sum = self._A + self._B
        self.notifyObservers()

    def addObserver(self, inObserver):
        self._Observers.append(inObserver)

    def removeObserver(self, inObserver):
        self._Observers.remove(inObserver)

    def notifyObservers(self):
        for x in self._Observers:
            x.modelIsChanged()


d = Model
d.a = 5
d.b = 7
print(d._Sum)
