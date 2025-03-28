from typing import List


class Solution:
    def findDuplicatesWithHashMap(self, nums: List[int]) -> List[int]:
        nums_map = {}
        for i in nums:
            if i not in nums_map:
                nums_map[i] = 1
            else:
                nums_map[i] += 1
        return list(filter(lambda x: nums_map[x] > 1, nums_map))

    def findDuplicatesWithHashSet(self, nums: List[int]) -> List[int]:
        seen = set()
        duplicates = []
        for num in nums:
            if num in seen:
                duplicates.append(num)
            seen.add(num)
        return duplicates

    def findDuplicates(self, nums: List[int]) -> List[int]:



sol = Solution()
print(sol.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
