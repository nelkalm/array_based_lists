# An ArrayStack implements the list interface using an array a, 
# called the backing array. The list element with index i is stored in a[i].

class ArrayStack:

    def __init__(self):
        self.lst = [None for element in range(5)]
        self.num_el = 0

    def get_num_el(self):
        return self.num_el

    def get_list(self):
        return self.lst

    def get_element(self, index):
        return self.lst[index]

    def set_element(self, index, value):
        y = self.lst[index]
        self.lst[index] = value
        return y

    def add_element(self, index, value):
        if self.num_el == len(self.lst):
            self.resize()
        for lst_idx in range(index + 1, self.num_el, 1):
            self.set_element(lst_idx + 1, self.lst[index])
        self.set_element(index, value)
        self.num_el += 1

    def remove_element(self, index):
        removed_element = self.lst[index]
        for lst_idx in range(index, self.num_el, 1):
            self.set_element(lst_idx, self.lst[lst_idx + 1])
        self.num_el -= 1
        return removed_element

    def resize(self):
        new_resized_list = [None for element in range(2 * self.num_el)]
        for index in range(len(self.lst)):
            new_resized_list[index] = self.lst[index]
        self.lst = new_resized_list
