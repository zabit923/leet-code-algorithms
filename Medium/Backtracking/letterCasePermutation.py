from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = [""]

        for char in s:
            tmp = []
            if char.isalpha():
                for i in res:
                    tmp.append(i + char.lower())
                    tmp.append(i + char.upper())
            else:
                for i in res:
                    tmp.append(i + char)
            res = tmp
        return res


sol = Solution()
print(sol.letterCasePermutation("a1b2"))
