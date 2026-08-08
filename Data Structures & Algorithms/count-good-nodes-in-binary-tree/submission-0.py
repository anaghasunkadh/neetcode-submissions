# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        def dfs(root,max_value):
            nonlocal count
            if root is None:
                return 
            if root.val>=max_value:
                max_value=max(root.val,max_value)
                count=count+1
            dfs(root.left,max_value)
            dfs(root.right,max_value)
            return count
        return dfs(root,root.val)

        