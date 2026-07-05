# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        stack=[]
        value=[]
        current=root
        while stack or current:
            if current is not None:
                stack.append(current)
                current=current.left
            elif current is None:
                element=stack.pop()
                value.append(element.val)
                current=element.right
        return value

            
        