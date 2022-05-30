class Stack:

    def __init__(self) -> None:
        self.stack = []

    # insert item into the stack
    def push(self, data):
        self.stack.append(data)

    # remove and return the last item we have inserted (LIFO) // O(1)
    def pop(self):
        if self.stack_size() < 1:
            return
        data = self.stack[-1]
        del self.stack[-1]
        return data

    # return the last item without removing it // O(1)
    def peek(self):
        return self.stack[-1]

    # check whether the stack is empty // O(1)
    def is_empty(self):
        return self.stack == []

    def stack_size(self):
        return len(self.stack)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(f'Stack size: {stack.stack_size()}')
print(f'Popped item: {stack.pop()}')
print(f'Stack size: {stack.stack_size()}')
print(f'Peeked item: {stack.peek()}')
