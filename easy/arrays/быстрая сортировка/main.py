from typing import List


def quick_sort(nums: List) -> List:
    if len(nums) <= 1:
        return nums
    num = nums[0]
    left = list(filter(lambda x: x < num, nums))
    center = [i for i in nums if i == num]
    right = list(filter(lambda x: x > num, nums))

    return quick_sort(left) + center + quick_sort(right)


print(quick_sort([3, 9, 5, 4, 6, 1, 7, 2, 8]))
