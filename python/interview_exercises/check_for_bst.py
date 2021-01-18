class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def check_bst(self):
        res = True
        if self.left is not None:
            if self.left.data <= self.data:
                res = self.left.check_bst()
            else:
                return False

        if self.right is not None:
            if self.right.data > self.data:
                res = self.right.check_bst()
            else:
                return False

        return res


if __name__ == '__main__':
    root = TreeNode(2)
    node7 = TreeNode(7)
    node6 = TreeNode(6)
    node5 = TreeNode(5)
    node9 = TreeNode(9)
    node2 = TreeNode(2)

    root = node6

    root.right = node7
    root.left = node5

    node7.left = node2
    node7.right = node9

    is_bst = root.check_bst()
    print(is_bst)
