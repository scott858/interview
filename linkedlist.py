class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        node = self.head
        while True:
            if node is None:
                break
            print(node.data)
            node = node.next

        print('\n')

    def pre_insert(self, node):
        node.next = self.head
        self.head = node

    def post_insert(self, node):
        if self.head is None:
            self.head = node
        else:
            next_node = self.head
            while True:
                if next_node.next is None:
                    break
                else:
                    next_node = next_node.next
        next_node.next = node

    def betwixt_insert(self, node, n):
        if self.head is None:
            self.head = node
        else:
            next_node = self.head
            while True:
                if next_node.next is None:
                    break
                else:
                    next_node = next_node.next
        next_node.next = node

        

if __name__ == '__main__':
    node1 = Node(data="Mon")
    node2 = Node(data="Tue")
    llist = LinkedList()
    llist.head = node1
    node1.next = node2

    llist.traverse()

    node3 = Node(data='Sun')
    llist.pre_insert(node3)
    llist.traverse()

    node4 = Node(data='Wed')
    llist.post_insert(node4)
    llist.traverse()
    
