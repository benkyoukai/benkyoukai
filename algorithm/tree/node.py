class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # Return int
    #
    #   if self < other, less than 0
    #   if self > other, greater than 0
    #   if self = other, 0
    def compare(self, other):
        raise Exception("not implemented")

    def less(self, other):
        return self.compare(other) < 0

    def greater(self, other):
        return self.compare(other) > 0

    def equal(self, other):
        return self.compare(other) == 0


class NumNode(Node):
    def compare(self, other):
        return self.val - other.val
