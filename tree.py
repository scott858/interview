import queue


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def add_node(self, data):
        if self.data:
            if data <= self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.add_node(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.add_node(data)

        else:
            self.data = data

    def print_tree(self):

        if self.left is not None:
            self.left.print_tree()

        print(self.data)

        if self.right is not None:
            self.right.print_tree()

    def in_order_traversal(self, root):
        visited = []

        if root is not None:
            visited += self.in_order_traversal(root.left)
            visited.append(root.data)
            visited += self.in_order_traversal(root.right)

        return visited

    def pre_order_traversal(self, root):
        visited = []

        if root is not None:
            visited.append(root.data)
            visited += self.pre_order_traversal(root.left)
            visited += self.pre_order_traversal(root.right)

        return visited

    def post_order_traversal(self, root):
        visited = []

        if root is not None:
            visited += self.post_order_traversal(root.left)
            visited += self.post_order_traversal(root.right)
            visited.append(root.data)

        return visited

    def bfs(self):
        q = queue.Queue()
        q.put(self)
        while not q.empty():
            node = q.get()
            print(node.data)
            if node.left is not None:
                q.put(node.left)
            if node.right is not None:
                q.put(node.right)


if __name__ == '__main__':
    root = Node(27)

    # l1
    root.add_node(14)
    # r1
    root.add_node(35)

    # l1-l2
    root.add_node(10)
    # l1-r2
    root.add_node(19)

    # r1-l2
    root.add_node(31)
    # r1-r2
    root.add_node(42)

    # root.print_tree()
    root.bfs()

    # trav = root.in_order_traversal(root)
    # print(trav)
    # trav = root.pre_order_traversal(root)
    # print(trav)
    # trav = root.post_order_traversal(root)
    # print(trav)
