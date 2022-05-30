class Queue:

    def __init__(self) -> None:
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, value):
        self.enqueue_stack.append(value)

    def dequeue(self):
        if len(self.enqueue_stack) == 0 and len(self.dequeue_stack) == 0:
            raise Exception("Stacks are empty ...")
        if len(self.dequeue_stack) == 0:
            while len(self.enqueue_stack) != 0:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        return self.dequeue_stack.pop()


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(5)
    queue.enqueue(20)

    # Print returns 10
    print(queue.dequeue())
