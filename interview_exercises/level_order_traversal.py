class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def traverse_level_order(self):
        queue = [self]

        while len(queue):
            node = queue.pop(0)
            if node is not None:
                print(node.data, end=' ')
                queue.append(node.left)
                queue.append(node.right)


def tree_three():
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node9 = TreeNode(9)

    root.left = node2
    root.right = node3

    node2.left = node4
    node2.right = node5

    node3.left = node6
    node3.right = node7

    node7.left = node8
    node7.right = node9
    return root


if __name__ == '__main__':
    root = tree_three()
    root.traverse_level_order()
