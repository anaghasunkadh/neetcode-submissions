# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        flag=True
        def height(curr):
            nonlocal flag
            if curr is None:
                return 0
            left=height(curr.left)
            right=height(curr.right)
            if abs(left-right)>1:
                flag= False
            return max(left,right)+1
        height(root)
        return flag

        