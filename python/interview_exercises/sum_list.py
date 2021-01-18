class SumListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def append_node(self, data):
        if self.data is None:
            self.data = data
        elif self.next is None:
            self.next = SumListNode(data)
        else:
            self.next.append_node(data)

    def create_number_list(self, number):
        digits = []
        while number > 0:
            digit = number % 10
            digits.append(digit)
            number /= 10
            number = int(number)

        while len(digits):
            self.append_node(digits.pop())

    def extract_digits(self, digits):
        digits.append(self.data)
        if self.next is not None:
            self.next.extract_digits(digits)

    def extract_number(self):
        digits = []
        self.extract_digits(digits)
        digits = digits[::-1]
        number = 0
        for i in range(len(digits)):
            number += int(digits[i] * 10 ** i)
        return number

    def add_list_number(self, node):
        number1 = self.extract_number()
        number2 = node.extract_number()
        sum = number1 + number2
        sum_node = SumListNode()
        sum_node.create_number_list(sum)
        return sum_node

    def print(self):
        print(self.data, end=' ')
        if self.next is not None:
            self.next.print()
        else:
            print()


