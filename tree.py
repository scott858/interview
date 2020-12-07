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
        

if __name__ == '__main__':
    root = Node(27)
    root.add_node(14)
    root.add_node(35)
    root.add_node(10)
    root.add_node(19)
    root.add_node(31)
    root.add_node(42)
    root.print_tree()
    #trav = root.in_order_traversal(root)
    #print(trav)
    #trav = root.pre_order_traversal(root)
    #print(trav)
    #trav = root.post_order_traversal(root)
    #print(trav)
