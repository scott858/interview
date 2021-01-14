class SpecialStack:
    def __init__(self, stack_size=100):
        self.stack = [0] * stack_size
        self.stack_pointer = -1
        self.stack_size = stack_size
        self.stack_min = 0

    def push(self, data):
        print('pushing {}'.format(data), end=' ')
        if self.stack_pointer < self.stack_size:
            self.stack_pointer += 1
            if self.stack_pointer == 0:
                self.stack_min = data
            elif data < self.stack_min:
                new_stack_min = data

                # encode
                data = 2 * data - self.stack_min

                self.stack_min = new_stack_min
                print(', new min found pushing {} instead'.format(data), end=' ')
            self.stack[self.stack_pointer] = data
        else:
            data = None
        print('')
        return data

    def pop(self):
        if self.stack_pointer >= 0:
            data = self.stack[self.stack_pointer]
            print('popping {}'.format(data), end=' ')
            if data < self.stack_min:
                old_stack_min = self.stack_min
                print(', popped stack min: {}'.format(old_stack_min))

                # decode
                self.stack_min = 2 * self.stack_min - data

                data = old_stack_min
            else:
                print('')
            self.stack_pointer -= 1
        else:
            data = None
        return data

    def is_full(self):
        return self.stack_pointer == self.stack_size

    def is_empty(self):
        return self.stack_pointer == 0

    def get_min(self):
        print('get min: {}'.format(self.stack_min))
        return self.stack_min
