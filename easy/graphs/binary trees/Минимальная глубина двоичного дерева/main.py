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
    def minDepth(self, root: Optional[TreeNode]) -> List[float]:



node7 = TreeNode(val=7, left=None, right=None)
node15 = TreeNode(val=15, left=None, right=None)
node9 = TreeNode(val=9, left=None, right=None)
node20 = TreeNode(val=20, left=node15, right=node7)
node3 = TreeNode(val=3, left=node9, right=node20)


sol = Solution()
print(sol.minDepth(node3))
