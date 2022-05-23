# Design an efficient algorithm to reverse a given integer.
# For example if the input of the algorithm is 1234 then the output should be 4321.

def reverse_integer(num):
    num_string = str(num)
    num_list = list(num_string)
    first_index = 0
    last_index = len(num_list) - 1

    while first_index < last_index:
        num_list[first_index], num_list[last_index] = num_list[last_index], num_list[first_index]
        first_index += 1
        last_index -= 1

    return int(''.join(num_list))


if __name__ == '__main__':
    print(reverse_integer(1234))
