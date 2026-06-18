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
        def getheight(root):
            if root is None:
                return 0
            left=getheight(root.left)
            right=getheight(root.right)
            height=max(left,right)+1
            return height
        left=getheight(root.left)
        right=getheight(root.right)
        if abs(left-right)>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
            
        