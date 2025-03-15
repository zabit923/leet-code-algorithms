from typing import List


def nextGreatestLetter(letters: List[str], target: str) -> str:
    l, r = 0, len(letters) - 1
    while l <= r:
        m = (l+r) // 2
        if letters[m] <= target:
            l = m + 1
        else:
            r = m - 1
    return letters[l] if l < len(letters) else letters[0]


print(nextGreatestLetter(["c", "f", "j"], "a"))
