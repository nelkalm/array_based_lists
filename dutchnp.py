# A program to sort a T[] one-dimensional array of integers in O(N) running time - and without any extra memory.
# The array can contain values: 0, 1 and 2.

def three_way_swap(array, pivot):
    i = 0
    j = 0
    k = len(array) - 1

    while j < k:
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
            j += 1
        elif array[j] > pivot:
            array[j], array[k] = array[k], array[j]
            k -= 1
        else:
            j += 1

    return array


if __name__ == '__main__':
    print(three_way_swap([1, 2, 0, 0, 2, 1, 2, 0], 1))
