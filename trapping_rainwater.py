# Given n non-negative integers representing an elevation map where the width of each bar is 1. Compute how much water it can trap after raining!


def water_trap(num_list):
    trapped_water = 0
    max_height = num_list[0]

    for index in range(1, len(num_list) - 1, 1):
        if num_list[index] < max_height:
            trapped_water += (max_height - num_list[index])
        else:
            max_height = num_list[index]
            trapped_water += (max_height - num_list[index])
    return trapped_water


if __name__ == '__main__':
    print(water_trap([4, 1, 3, 1, 5]))
    print(water_trap([2, 1, 3, 1, 4]))
    print(water_trap([1, 0, 2, 1, 3, 1, 2, 0, 3]))
