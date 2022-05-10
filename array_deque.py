# An ArrayDeque implements the List interface, based on pseudocode provided in section 2.4
# of OpenDataStructures.

class ArrayDeque:

    def __init__(self) -> None:
        self.array = [None for element in range(5)]
        self.index = 0
        self.num_elements = 0

    def get_value(self, desired_index):
        return self.array[(desired_index + self.index) % len(self.array)]

    def set_value(self, desired_index, value):
        value_set = self.array[(desired_index + self.index) % len(self.array)]
        self.array[(desired_index + self.index) % len(self.array)] = value
        return value_set

    def add_element(self, desired_index, value):
        if self.num_elements == len(self.array):
            self._resize()
        if desired_index < self.num_elements / 2:
            self.index = (self.index - 1) % len(self.array)
            for k in range(0, desired_index - 1, 1):
                self.array[(self.index + k) % len(self.array)
                           ] = self.array[(self.index + k + 1) % len(self.array)]
        else:
            for k in range(self.num_elements, desired_index + 1, -1):
                self.array[(self.index + k) % len(self.array)
                           ] = self.array[(self.index + k + 1) % len(self.array)]
        self.array[(self.index + desired_index) % len(self.array)] = value
        self.num_elements += 1

    def remove_element(self, desired_index):
        removed_value = self.array[(
            self.index + desired_index) % len(self.array)]
        if desired_index < self.num_elements / 2:
            for k in range(desired_index, 1, -1):
                self.array[(self.index + k) % len(self.array)
                           ] = self.array[(self.index + k - 1) % len(self.array)]
            self.index = (self.index + 1) % len(self.array)
        else:
            for k in range(desired_index, self.num_elements - 2, 1):
                self.array[(self.index + k) % len(self.array)
                           ] = self.array[(self.index + k + 1) % len(self.array)]
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


my_array = ArrayDeque()
print(my_array.array)
my_array.add_element(0, 'a')
my_array.add_element(1, 'b')
my_array.add_element(2, 'c')
my_array.add_element(3, 'd')
my_array.add_element(4, 'e')
my_array.add_element(5, 'f')
print(my_array.array)
my_array.remove_element(2)
print(my_array.array)
my_array.add_element(4, 'x')
print(my_array.array)

