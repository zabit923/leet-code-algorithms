from typing import Optional, List


"""
Вход: корень = [1,2,3,null,5]
Выход: ["1->2->5","1->3"]
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        result = []

        def dfs(head: TreeNode, string: str, res: List[str]):
            string += str(head.val)
            if head.left:
                dfs(head.left, string+"->", res)
            if head.right:
                dfs(head.right, string+"->", res)
            if not head.left and not head.right:
                res.append(string)

        dfs(root, "", result)
        return result


node5 = TreeNode(5, None, None)
node3 = TreeNode(3, None, None)
node2 = TreeNode(2, None, node5)
node1 = TreeNode(1, node2, node3)


sol = Solution()
print(sol.binaryTreePaths(node1))
