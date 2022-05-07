# array_queue.py is an ArrayQueue implementation based on pseudocode and content
# presented in chapter 2.3 of Open Data Structures. An ArrayQueue implements
# the (FIFO) Queue interface.

from array_stack import ArrayStack


class ArrayQueue:

    def __init__(self) -> None:
        self.array = [None, None, 'a', 'b', 'c', None]
        self.index = 2
        self.num_elements = 3

    def get_array(self):
        return self.array

    # def set_element(self, index, value):
    #     y = self.array[index]
    #     self.array[index] = value
    #     return y

    def add(self, value):
        if self.num_elements + 1 > len(self.array):
            self.resize()
        self.array[(self.index + self.num_elements) % len(self.array)] = value
        self.num_elements += 1
        return True

    def remove(self):
        removed_value = self.array[self.index]
        self.index = (self.index + 1) % len(self.array)
        self.num_elements -= 1
        if len(self.array) >= 3 * self.num_elements:
            self.resize()
        return removed_value

    def resize(self):
        resized_array = [None for element in range(len(self.array) * 2)]
        for i in range(self.num_elements - 1):
            resized_array[i] = self.array[(self.index + i) % len(self.array)]
        self.array = resized_array
        self.index = 0


my_array = ArrayQueue()
print(my_array.get_array())
my_array.add('d')
print(my_array.get_array())
my_array.add('e')
print(my_array.get_array())
my_array.add('f')
print(my_array.get_array())
my_array.add('g')
print(my_array.get_array())