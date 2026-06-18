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
        stack=[]
        visited_list=[]
        stack.append(root)
        while stack:
            element=stack.pop()
            visited_list.append(element.val)
            if element.left is not None:
                stack.append(element.left)
            if element.right is not None:
                stack.append(element.right)
        visited_list.reverse()
        return visited_list
        