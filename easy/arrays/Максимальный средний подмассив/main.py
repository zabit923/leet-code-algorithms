from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        cur_sum = sum(nums[:k])

        max_avg = cur_sum / k

        for i in range(k, n):
            cur_sum += nums[i]
            cur_sum -= nums[i - k]
            avg = cur_sum / k
            max_avg = max(max_avg, avg)

        return max_avg


sol = Solution()
print(sol.findMaxAverage([1, 12, -5, -6, 50, 3], 4))
