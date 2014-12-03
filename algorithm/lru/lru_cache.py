class _Node:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.nodes = {}
        self.capacity = capacity
        self.size = 0

        # For the double linked list
        #
        # [N1] <-> [N2] <-> ... <-> [Nm]
        #  ^                         ^
        # head                      tail
        self.tail = None
        self.head = None

    # [Public]
    #
    # key -> Bool
    def has_key(self, key):
        return self.nodes.has_key(key)

    # [Public]
    #
    # None -> Bool
    def full(self):
        return self.size >= self.capacity

    # [Public]
    #
    # key -> value|None
    def get(self, key):
        if self.has_key(key):
            node = self.nodes[key]
            self.touch(node)
            return self.nodes[key].value

    # [Public]
    #
    # key, value -> LRUCache
    def set(self, key, value):
        if self.has_key(key):
            node = self.nodes[key]
            self.touch(node)
            node.value = value
        else:
            if self.full():
                self.delete(self.head.key)
            self.size += 1
            node = _Node(key, value)
            self.nodes[key] = node
            self.append(node)
        return self

    # [Public]
    #
    # key -> value|None
    def delete(self, key):
        if self.has_key(key):
            self.size -= 1
            node = self.nodes[key]
            self.remove(node)
            del self.nodes[key]
            return node.value

    # The followings are internal APIs
    # They are used to maintain a double linked list which
    # in turn keeps all the nodes in LRU-order.
    #
    # Internal API should only manipulates the
    # `head', `tail' and its own param. They have nothing
    # to do with the `size', `capacity', or `nodes'.

    # [Internal] mark a node as the most recently used
    #
    # _Node -> LRUCache
    def touch(self, node):
        self.remove(node)
        return self.append(node)

    # [Internal] remove a node from double linked list
    #
    # _Node -> _Node
    def remove(self, node):
        if node == self.head:
            self.head = node.next
        elif node == self.tail:
            self.tail = node.prev
        else:
            n1 = node.prev
            n2 = node.next
            if n1:
                n1.next = n2
            if n2:
                n2.prev = n1
        return node

    # [Internal] append a new node to double linked list
    #
    # _Node -> LRUCache
    def append(self, node):
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        return self
