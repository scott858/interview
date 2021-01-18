class TreeNode:
    """
    Can also be done with a linked hash with keys of horizontal distance
    """
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def traverse_vertical(self, stack=None):
        if stack is None:
            stack = [self]

        if self.left is not None:
            stack.append(self.left)
            self.left.traverse_vertical(stack)

        print_stack(stack)

        if self.right is not None:
            stack.insert(0, self.right)
            self.right.traverse_vertical(stack)

        print_stack(stack)


def print_stack(stack):
    while len(stack):
        node = stack.pop()
        if node is not None:
            print(node.data, end=' ')


def tree_one():
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)

    root.left = node2
    root.right = node3

    node2.left = node4
    node2.right = node5

    node3.right = node6
    return root


def tree_two():
    root = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)

    root.right = node3
    node3.left = node4

    return root


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
    # root = tree_one()
    # root = tree_two()
    root = tree_three()
    root.traverse_vertical()
