from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        res = []
        for r in range(m):
            start = r * n
            end = start + n
            res.append(original[start:end])
        return res


sol = Solution()
print(sol.construct2DArray([1, 2, 3, 4, 5, 6], 2, 3))
