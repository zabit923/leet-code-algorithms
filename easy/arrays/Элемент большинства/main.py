from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]


sol = Solution()
print(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]))
