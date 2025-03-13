from typing import List


def missingNumber(nums: List[int]) -> int:
    count = len(nums)
    nums.sort()
    result = 0
    for i in range(1, count + 1):
        if i not in nums:
            result = i
    return result


print(missingNumber([3, 0, 1]))
