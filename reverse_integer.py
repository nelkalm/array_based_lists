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


# Use the modullo operator to get the last digit
def reverse_integer_efficient(num):
    reversed_integer = 0
    remainder = 0

    while num > 0:
        remainder = num % 10
        reversed_integer = reversed_integer * 10 + remainder
        num //= 10

    return reversed_integer


if __name__ == '__main__':
    print(reverse_integer(1234))
    print(reverse_integer_efficient(1234))
