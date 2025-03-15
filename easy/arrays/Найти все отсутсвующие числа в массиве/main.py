from typing import List


def findDisappearedNumbers(nums: List[int]) -> List[int]:
    count = len(nums)
    nums.sort()
    result = []
    for i in range(1, count + 1):
        if i not in nums:
            result.append(i)
    return result


print(findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
