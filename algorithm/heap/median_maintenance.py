import sys
import os
sys.path.append(os.path.abspath("heap"))

from heap import Heap

class MedianMaintainer:
    def __init__(self, elems, cmp=cmp):
        self.cmp = cmp
        self.high = Heap([], cmp)
        self.low = Heap([], lambda x,y: cmp(y, x))

        for el in elems:
            self.insert(el)

    def insert(self, elem):
        if self.high.size() == 0:
            self.high.insert(elem)
            return

        h = self.high.findmin()
        if cmp(elem, h) > 0:
            self.high.insert(elem)
        else:
            self.low.insert(elem)

        self._balance()
        return self

    def peek(self):
        return self._get_large_heap().findmin()

    def _get_large_heap(self):
        if self.low.size() > self.high.size():
            return self.low
        else:
            return self.high

    def _balance(self):
        if self.high.size() - self.low.size() > 1:
            tmp = self.high.popmin()
            self.low.insert(tmp)
        elif self.low.size() - self.high.size() > 1:
            tmp = self.low.popmin()
            self.high.insert(tmp)


if __name__ == "__main__":
    m = MedianMaintainer(list(range(1,100)))
    print m.low.size()
    print m.high.size()
    print m.peek()

