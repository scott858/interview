class TreeNode:
    largest = None

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def max_diff(self, smallest_value=None):

        if self.left is not None:
            res = self.left.max_diff()
            if smallest_value is None or res < smallest_value:
                smallest_value = res

        if self.right is not None:
            res = self.right.max_diff()
            if smallest_value is None or res < smallest_value:
                smallest_value = res

        if smallest_value is not None:
            # print(self.data - smallest_value)
            diff = self.data - smallest_value
            if TreeNode.largest is None or TreeNode.largest < diff:
                TreeNode.largest = diff

        if smallest_value is None or self.data < smallest_value:
            smallest_value = self.data

        return smallest_value


if __name__ == '__main__':
    root = TreeNode(1)
    node2 = TreeNode(2)
    node1 = TreeNode(1)
    node3 = TreeNode(3)
    node7 = TreeNode(7)

    root.left = node2
    root.right = node3

    node3.right = node7

    root.max_diff()
    print(TreeNode.largest)
