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
        value=[]
        value.append(root.val)
        value.extend(self.preorderTraversal(root.left))
        value.extend(self.preorderTraversal(root.right))
        return value
        