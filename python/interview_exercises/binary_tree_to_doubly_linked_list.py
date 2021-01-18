prev_node = None


class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def linkify(self):
        global prev_node
        if self.left is not None:
            self.left.linkify()

        self.left = prev_node
        if prev_node is not None:
            prev_node.right = self
        prev_node = self

        if self.right is not None:
            self.right.linkify()

    def print_dll(self):
        start_node = self
        while start_node.left is not None:
            start_node = start_node.left
        TreeNode.traverse_right_print(start_node)

        while start_node.right is not None:
            start_node = start_node.right
        TreeNode.traverse_left_print(start_node)

    @staticmethod
    def traverse_right_print(start_node):
        print(start_node.data, ' ', end=' ')
        if start_node.right is not None:
            TreeNode.traverse_right_print(start_node.right)

    @staticmethod
    def traverse_left_print(start_node):
        print(start_node.data, ' ', end=' ')
        if start_node.left is not None:
            TreeNode.traverse_left_print(start_node.left)


