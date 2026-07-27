# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        value=[]
        stack=[]
        stack.append(root)
        while stack:
            ele=stack.pop()
            value.append(ele.val)
            if ele.left:
                stack.append(ele.left)
            if ele.right:
                stack.append(ele.right)
        return value[::-1]
        