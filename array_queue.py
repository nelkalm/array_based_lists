# array_queue.py is an ArrayQueue implementation based on pseudocode and content
# presented in chapter 2.3 of Open Data Structures. An ArrayQueue implements
# the (FIFO) Queue interface.


class ArrayQueue:

    def __init__(self) -> None:
        self.array = [None for element in range(6)]
        self.index = 0
        self.num_elements = 0

    def add(self, value):
        if self.num_elements + 1 > len(self.array):
            self._resize()
        self.array[(self.index + self.num_elements) % len(self.array)] = value
        self.num_elements += 1
        return True

    def remove(self):
        removed_value = self.array[self.index]
        self.index = (self.index + 1) % len(self.array)
        self.num_elements -= 1
        if len(self.array) >= 3 * self.num_elements:
            self._resize()
        return removed_value

    def _resize(self):
        resized_array = [None for element in range(len(self.array) * 2)]
        for i in range(self.num_elements):
            resized_array[i] = self.array[(self.index + i) % len(self.array)]
        self.array = resized_array
        self.index = 0


my_array = ArrayQueue()
my_array.add('a')
my_array.add('b')
my_array.add('c')
my_array.add('d')
my_array.add('e')
my_array.add('f')
my_array.add('g')
my_array.add('h')

print(my_array.array)
