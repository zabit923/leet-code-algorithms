from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if (p and p.val) != (q and q.val):
            return False
        return (
            self.isSameTree(p.left, q.left)
            and
            self.isSameTree(p.right, q.right)
        )


node3 = TreeNode(val=3, left=None, right=None)
node2 = TreeNode(val=2, left=None, right=None)
node1 = TreeNode(val=1, left=node2, right=node3)

node6 = TreeNode(val=3, left=None, right=None)
node5 = TreeNode(val=2, left=None, right=None)
node4 = TreeNode(val=1, left=node5, right=node6)


sol = Solution()
print(sol.isSameTree(node1, node4))
