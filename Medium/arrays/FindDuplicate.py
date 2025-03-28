from typing import List


class Solution:
    def findDuplicateWithHash(self, nums: List[int]) -> int:
        nums_map = {}
        for i in nums:
            if i not in nums_map:
                nums_map[i] = 1
            else:
                nums_map[i] += 1
        return max(nums_map, key=nums_map.get)

    def findDuplicateWithoutHash(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


sol = Solution()
print(sol.findDuplicateWithoutHash([1, 3, 4, 2, 2]))
