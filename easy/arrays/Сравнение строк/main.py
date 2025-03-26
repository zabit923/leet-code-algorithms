

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def line_formation(input_str: str):
            result = []
            for char in input_str:
                if char != "#":
                    result.append(char)
                elif result:
                    result.pop()
            return result
        return line_formation(s) == line_formation(t)


sol = Solution()
print(sol.backspaceCompare("ab#c", "ad#c"))
