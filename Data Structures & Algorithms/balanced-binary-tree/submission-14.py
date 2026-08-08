# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag=True
        if root is None:
            return True
        def height(curr):
            nonlocal flag
            if curr is None:
                return True
            left=height(curr.left)
            right=height(curr.right)
            if abs(left-right)>1:
                flag=False
            he=max(left,right)+1
            return he
        height(root)
        return flag

        