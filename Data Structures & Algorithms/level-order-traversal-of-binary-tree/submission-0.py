# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue =collections.deque()
        value=[]
        queue.append(root)
        while queue:
            level=[]
            size=len(queue)
            for i in range(size):
                element = queue.popleft()
                level.append(element.val)
                if element.left is not None:
                    queue.append(element.left)
                if element.right is not None:
                    queue.append(element.right)
            value.append(level)
        return value
        