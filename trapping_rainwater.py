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


# Dynamic programming approach
def water_trap_efficient(heights):
    if len(heights) < 3:
        return 0

    left_max = [0 for _ in range(len(heights))]
    right_max = [0 for _ in range(len(heights))]

    # left max items
    for i in range(1, len(heights)):
        left_max[i] = max(left_max[i - 1], heights[i - 1])

    # right max items
    for i in range(len(heights) - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], heights[i + 1])

    # consider items in O(N) and sum up the trapped rain water units
    trapped = 0

    for i in range(1, len(heights) - 1):
        if min(left_max[i], right_max[i]) > heights[i]:
            trapped += min(left_max[i], right_max[i]) - heights[i]


if __name__ == '__main__':
    print(water_trap([4, 1, 3, 1, 5]))
    print(water_trap([2, 1, 3, 1, 4]))
    print(water_trap([1, 0, 2, 1, 3, 1, 2, 0, 3]))
