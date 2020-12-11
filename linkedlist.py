class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def print(self):
        node_str = str(self.data) + ', '
        root = self.next
        while root:
            node_str += str(root.data) + ', '
            root = root.next

        print(node_str)

    def pre_insert(self, data):
        node = Node(data)
        temp_node = self.next
        node.next = temp_node
        self.next = node

    def post_insert(self, data):
        root = self
        while root.next:
            root = root.next

        root.next = Node(data)

    def insert_at(self, n, data):
        if n > 0:
            node_n_minus_1 = self.get_at(n - 1)
            node_n_plus_1 = node_n_minus_1.next
            node_n = Node(data)
            node_n.next = node_n_plus_1
            node_n_minus_1.next = node_n

    def get_at(self, n):
        node = self
        while node.next and n > 0:
            node = node.next
            n -= 1

        return node

    def pre_delete(self):
        delete_this = self.next
        if delete_this:
            self.next = delete_this.next
            del delete_this

    def post_delete(self):
        root = self
        if root.next:
            while root.next.next:
                root = root.next

            delete_this = root.next
            root.next = None
            del delete_this

    def delete_at(self, n):
        node_n_minus_1 = self.get_at(n-1)
        if node_n_minus_1.next:
            node_n_plus_1 = node_n_minus_1.next.next
            delete_this = node_n_minus_1.next
            node_n_minus_1.next = node_n_plus_1
            del delete_this


if __name__ == '__main__':
    data = [1, 4, 6, 3, 42, 7, 9, 44, 2]

    root = Node(0)
    for d in data:
        root.post_insert(d)

    for i in range(len(data) + 1):
        root.print()
        root.delete_at(1)
