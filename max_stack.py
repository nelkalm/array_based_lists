# Get the max item pushed onto a stack
# O(1) running time. O(N) space complexity.

class MaxStack:

    def __init__(self) -> None:
        self.main_stack = []
        self.max_stack = []

    def push(self, value):
        self.main_stack.append(value)

        if len(self.main_stack) == 1 or value > self.max_stack[-1]:
            self.max_stack.append(value)
        else:
            self.max_stack.append(self.max_stack[-1])

    def pop(self):
        self.max_stack.pop()
        return self.main_stack.pop()

    def get_max_item(self):
        return self.max_stack.pop()


max_stack = MaxStack()
max_stack.push(1)
max_stack.push(2)
max_stack.push(1)
max_stack.push(3)
print(max_stack.main_stack)
print(max_stack.max_stack)
print(max_stack.get_max_item())
