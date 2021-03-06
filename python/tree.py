class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def bst_add(self, data):
        """
        O(log(n))
        :param data:
        :return:
        """
        if self.data is None:
            root.data = data
        else:
            node = Node(data)
            if data <= self.data:
                if self.left:
                    self.left.bst_add(data)
                else:
                    self.left = node
            else:
                if self.right:
                    self.right.bst_add(data)
                else:
                    self.right = node

    @staticmethod
    def dfs_in_order(node):
        if node:
            Node.dfs_in_order(node.left)
            print(node.data, end=' ')
            Node.dfs_in_order(node.right)

    @staticmethod
    def dfs_pre_order(node):
        if node:
            print(node.data, end=' ')
            Node.dfs_pre_order(node.left)
            Node.dfs_pre_order(node.right)

    @staticmethod
    def dfs_post_order(node):
        if node:
            Node.dfs_post_order(node.left)
            Node.dfs_post_order(node.right)
            print(node.data, end=' ')

    def bfs(self):
        """
        O(log(n))
        :return:
        """
        node_q = [self]
        next_node_q = []
        data_str = str(self.data) + '\n'
        while len(node_q):
            node = node_q.pop(0)
            data_str += self.add_children(next_node_q, node)

            if len(node_q) == 0:
                data_str += '\n'
                node_q = next_node_q
                next_node_q = []

        print(data_str)

    def add_children(self, node_q, node):
        data_str = ''
        if node.left:
            node_q.append(node.left)
            data_str += 'l' + str(node.left.data) + ' '
        else:
            data_str += 'l  '
        if node.right:
            node_q.append(node.right)
            data_str += 'r' + str(node.right.data) + ' '
        else:
            data_str += 'r  '
        return data_str

    @staticmethod
    def sort(node):
        """
        time: O(n*log(n))
        :param node:
        :return:
        """
        return Node.dfs_in_order(node)

    @staticmethod
    def delete(root):
        if root:
            Node.delete(root.left)
            Node.delete(root.right)
            root.left = None
            root.right = None
            root = None


if __name__ == '__main__':
    data = [5, 6, 7, 8, 2, 3, 4, ]

    root = Node(0)
    # for d in data:
    #     root.bst_add(d)
    #
    # print(Node.sort(root))
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    root.left = node1
    root.right = node2

    node1.left = node3
    node1.right = node4

    node2.left = node5

    root.dfs_in_order(root)
    print()
    root.dfs_pre_order(root)
    print()
    root.dfs_post_order(root)
