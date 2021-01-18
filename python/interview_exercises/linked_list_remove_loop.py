class ListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def print_list(self):
        print(self.data)
        if self.next is not None:
            self.next.print_list()

    def deloop(self, loop_position, loop_node=None):
        if loop_node is None and loop_position == 0:
            return
        if loop_position == 1:
            loop_node = self

        if self.next == loop_node:
            self.next = None
        elif self.next is None:
            pass
        else:
            self.next.deloop(loop_position - 1, loop_node)


if __name__ == '__main__':
    root = ListNode(1)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node8 = ListNode(8)

    root.next = node3
    node3.next = node4
    node4.next = node3

    root.deloop(0)
    # root.print_list()
