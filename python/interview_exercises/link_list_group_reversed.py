class ListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def generate(self, data):
        for d in data:
            self.add(d)

    def add(self, data):
        if self.data is None:
            self.data = data
        elif self.next is None:
            self.next = ListNode(data)
        else:
            self.next.add(data)

    def print(self):
        print(self.data, end=' ')
        if self.next is not None:
            self.next.print()
        else:
            print('\n')

    def group_reverse(self, k, group_nodes=None):
        if group_nodes is None:
            group_nodes = []

        group_nodes.append(self)

        if len(group_nodes) == k or self.next is None:
            group_values = [n.data for n in group_nodes[::-1]]
            for val, node in zip(group_values, group_nodes):
                node.data = val
            group_nodes = []

        if self.next is not None:
            self.next.group_reverse(k, group_nodes)
