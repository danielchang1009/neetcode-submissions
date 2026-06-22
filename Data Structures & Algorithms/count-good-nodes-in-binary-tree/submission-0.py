# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,maxnode):
            if not node:
                return 0
            if node.val>=maxnode:
                res=1
            else:
                res=0
            maxnode=max(node.val,maxnode)
            res+=dfs(node.left,maxnode)
            res+=dfs(node.right,maxnode)
            return res

        return dfs(root,root.val)
        