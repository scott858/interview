class DoublyLinkedList:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class LruCache:
    def __init__(self, capacity=256):
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.hash_size = 10000
        self.cache = [None] * self.hash_size

    def get(self, data_pos):
        data_ix = data_pos - 1
        data_ix %= self.hash_size

        node = self.cache[data_ix]
        if node is not None:
            data = node.data[1]
        else:
            data = -1
        print('GET {0}->{1}'.format(data_pos, data))
        return data

    def set(self, data_pos, data):
        data_ix = data_pos - 1
        data_ix %= self.hash_size

        new_head = self.cache[data_ix]
        if new_head is not None:
            new_head.data = (data_ix, data)
            prev_node = new_head.prev
            next_node = new_head.next
            if prev_node is not None:
                prev_node.next = next_node
            next_node.prev = prev_node
        else:
            new_head = DoublyLinkedList((data_ix, data))
            if self.head is None:
                self.head = new_head
                self.tail = new_head
            if self.capacity > 0:
                self.capacity -= 1
            else:
                self.cache[self.tail.data[0]] = None
                new_tail = self.tail.next
                new_tail.prev = None
                self.tail.next = None
                self.tail = new_tail

        self.head.next = new_head
        self.head = new_head
        self.cache[data_ix] = new_head
        print('SET {0}->{1}'.format(data_pos, data))


if __name__ == '__main__':
    lru = LruCache(capacity=2)

    lru.set(1, 2)

    lru.set(2, 3)
    lru.set(1, 5)
    lru.set(4, 5)
    lru.set(6, 7)
    lru.get(4)

    lru.get(1)
