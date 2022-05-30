class Queue:
    def __init__(self) -> None:
        self.queue = []

    # O(1)
    def is_empty(self):
        return self.queue == []

    # O(1)
    def enqueue(self, data):
        self.queue.append(data)

    # O(N). Linked list would be better here
    def dequeue(self):
        if self.size_queue() != 0:
            data = self.queue[0]
            del self.queue[0]
            return data
        return

    # O(1)
    def peek(self):
        return self.queue[0]

    # O(1)
    def size_queue(self):
        return len(self.queue)


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(f'Size: {queue.size_queue()}')
print(f'Dequeue: {queue.dequeue()}')
print(f'Size: {queue.size_queue()}')
