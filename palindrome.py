# Design an optimal algorithm for checking whether a given string is palindrome

def is_palindrome(str):

    first_index = 0
    last_index = len(str) - 1
    match = 0

    while first_index < last_index:
        if str[first_index] == str[last_index]:
            match += 1
        first_index += 1
        last_index -= 1

    if int(len(str) / 2) == match:
        return True
    return False


def is_palindrome_2(str):
    if str == str[::-1]:
        return True
    return False


if __name__ == '__main__':
    print(is_palindrome('radar'))
