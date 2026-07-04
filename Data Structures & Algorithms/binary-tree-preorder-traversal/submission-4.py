# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        stack=[]
        value=[]
        stack.append(root)
        while stack:
            element=stack.pop()
            value.append(element.val)
            if element.right:
                stack.append(element.right)
            if element.left:
                stack.append(element.left)
        return value


        