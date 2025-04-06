from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:



sol = Solution()
print(sol.exist(
    [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ],
    "ABCCED"
))
