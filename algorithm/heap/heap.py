# Basic min-heap data structure
#
# API
#
#   Heap([elem...]) -> Heap
#   insert(elem)    -> Heap
#   findmin(elem)   -> elem
#   popmin(elem)    -> elem
#   size()          -> int
#   value()         -> list of elem
#
# Element comparison uses the general comparison operators.
class Heap:
    def __init__(self, elems=[]):
        self._elems = []
        self._size = 0

        for el in elems:
            self.insert(el)

    def insert(self, el):
        self._size += 1
        self._elems.append(el)
        self._siftup()
        return self

    def findmin(self, el):
        return self._elems[0]

    def popmin(self):
        self._size -= 1
        # save current min element
        m = self._elems[0]
        # move last element to top
        self._elems[0] = self._elems[-1]
        # delete last element
        del self._elems[-1]
        # sift down
        self._siftdown()
        return m

    def size(self):
        return self._size

    def value(self):
        return self._elems

    def _siftup(self):
        i = self._size - 1
        pi = (i-1) / 2
        elems = self._elems

        while i != 0 and elems[pi] > elems[i]:
            # swap
            elems[pi], elems[i] = elems[i], elems[pi]
            i, pi = pi, (pi-1) / 2

    def _siftdown(self):
        i = 0
        elems = self._elems

        while True:
            li, ri = 2 * i + 1, 2 * i + 2
            # no left or right child
            if li >= self._size:
                return

            # default left child
            j = li
            # right child exists and less than the left child
            if ri <= self._size and elems[li] > elems[ri]:
                j = ri

            # parent is less than children then it's done.
            if elems[i] <= elems[j]:
                return

            # swap
            elems[i], elems[j] = elems[j], elems[i]
            i = j

if __name__ == "__main__":
    h = Heap([3,8,1])
    print h.value()
    h.insert(6)
    h.insert(7)
    h.insert(5)
    print h.value()
    h.popmin()
    print h.value()
    h.popmin()
    print h.value()
    h.insert(6)
    print h.value()
    h.popmin()
    print h.value()

