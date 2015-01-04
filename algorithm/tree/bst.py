import sys
import os
sys.path.append(os.path.abspath("node"))
from node import Node
from node import NumNode

class BST:
    def __init__(self, val, Node=Node):
        self.root = Node(val)
        self.Node = Node
        self.size = 1

    def insert(self, val):
        self._insert(self.root, self.Node(val))
        self.size += 1
        return self

    def find(self, val):
        return self._find(self.root, self.Node(val))

    def delete(self, val):
        #      meta
        #     /
        #  root
        #  /   \
        # ...  ...
        meta = self.Node(None, self.root)
        node = self.Node(val)

        if self._delete(meta, self.root, node):
            self.size -= 1
            self.root = meta.left
            return True

        return False

    # Recursive helper functions
    def _insert(self, root, node):
        if node.less(root):
            if not root.left:
                root.left = node
            else:
                self._insert(root.left, node)
        else:
            if not root.right:
                root.right = node
            else:
                self._insert(root.right, node)

    def _find(self, root, node):
        if root is None:
            return None

        if node.less(root):
            return self._search(root.left, node)
        elif node.greater(root):
            return self._search(root.right, node)
        else:
            return root

    def _delete(self, parent, root, node):
        if root is None:
            return None

        if node.equal(root):
            if root.left and root.right:
                self._d2(parent, root)
            elif root.left or root.right:
                self._d1(parent, root)
            else:
                self._d0(parent, root)
            return True

        return self._delete(root, root.left, node) or self._delete(root, root.right, node)

    def _d0(self, parent, root):
        if parent.left and root.equal(parent.left):
            parent.left = None
        else:
            parent.right = None

    def _d1(self, parent, root):
        child = root.left or root.right

        if parent.left and root.equal(parent.left):
            parent.left = child
        else:
            parent.right = child

    def _d2(self, _, root):
        pre, cur = root, root.left
        while cur.right:
            pre, cur = cur, cur.right

        root.val = cur.val
        self._d1(pre, cur)


if __name__ == "__main__":
    putc = sys.stdout.write

    # tree:
    #       1
    #      /  \
    #    -2    3
    #    /    / \
    #  -3    2   4
    def tree():
        tree = BST(1, NumNode)
        tree.insert(3)
        tree.insert(2)
        tree.insert(4)
        tree.insert(-2)
        tree.insert(-3)
        return tree

    def ptree(tree):
        nodes = [tree.root]
        while any(nodes):
            new_nodes = []

            for node in nodes:
                if node:
                    new_nodes.append(node.left)
                    new_nodes.append(node.right)
                    putc(str(node.val))
                    putc(" ")
                else:
                    putc("# ")
            nodes = new_nodes
            print

    print "# original"
    ptree(tree())
    print

    print "# delete -2"
    t = tree()
    t.delete(-2)
    ptree(t)
    print

    print "# delete -3"
    t = tree()
    t.delete(-3)
    ptree(t)
    print

    print "# delete 3"
    t = tree()
    t.delete(3)
    ptree(t)
    print

    print "# delete 1"
    t = tree()
    t.delete(1)
    ptree(t)
    print

    print "# delete None"
    t = tree()
    t.delete(10000)
    ptree(t)
    print
