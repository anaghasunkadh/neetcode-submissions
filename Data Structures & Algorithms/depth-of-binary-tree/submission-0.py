# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue=collections.deque()
        value=[]
        queue.append(root)
        counter=0
        while queue:
            size=len(queue)
            level=[]
            for i in range(size):
                element=queue.popleft()
                level.append(element)
                if element.left is not None:
                    queue.append(element.left)
                if element.right is not None:
                    queue.append(element.right)
            counter=counter+1
        return counter
            
        