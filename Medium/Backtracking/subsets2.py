from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def create_subset(i: int, subset: List[int]):
            if i == len(nums):
                res.append(subset[:])
                return

            subset.append(nums[i])
            create_subset(i+1, subset)
            subset.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            create_subset(i+1, subset)
        create_subset(0, [])
        return res


sol = Solution()
print(sol.subsetsWithDup([1, 2, 2]))
