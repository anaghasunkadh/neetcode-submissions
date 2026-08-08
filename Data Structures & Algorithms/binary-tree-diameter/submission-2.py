# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter=0
        if root is None:
            return 0
        def height(curr):
            nonlocal diameter
            if curr is None:
                return 0
            left=height(curr.left)
            right=height(curr.right)
            value=left+right
            diameter=max(diameter,value)
            he= max(left,right)+1
            return he
        height(root)
        return diameter
        