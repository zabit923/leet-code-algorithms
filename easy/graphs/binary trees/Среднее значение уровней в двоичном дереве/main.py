from typing import Optional, List


"""
[3,9,20,null,null,15,7]

        3
      /   \
     9    20
        /    \
       15     7
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        avgs = []
        curr = [root]
        while curr:
            new_level = []
            curr_sum = 0
            for r in curr:
                if r.right:
                    new_level.append(r.right)
                if r.left:
                    new_level.append(r.left)
                curr_sum += r.val
            avgs.append(curr_sum/len(curr))
            curr = new_level
        return avgs


node7 = TreeNode(val=7, left=None, right=None)
node15 = TreeNode(val=15, left=None, right=None)
node9 = TreeNode(val=9, left=None, right=None)
node20 = TreeNode(val=20, left=node15, right=node7)
node3 = TreeNode(val=3, left=node9, right=node20)


sol = Solution()
print(sol.averageOfLevels(node3))
