from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            desire = target - num
            if desire in num_map:
                return [num_map[desire], i]
            num_map[num] = i


sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
