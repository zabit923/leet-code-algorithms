from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(curr: TreeNode):
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, left+right)
            return 1 + max(left, right)
        dfs(root)
        return self.res


node5 = TreeNode(val=5, left=None, right=None)
node4 = TreeNode(val=4, left=None, right=None)
node3 = TreeNode(val=3, left=None, right=None)
node2 = TreeNode(val=2, left=node4, right=node5)
node1 = TreeNode(val=1, left=node2, right=node3)


sol = Solution()
print(sol.diameterOfBinaryTree(node1))
