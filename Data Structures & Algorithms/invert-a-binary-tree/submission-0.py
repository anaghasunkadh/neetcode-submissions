# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue=collections.deque()
        queue.append(root)
        if root is None:
            return None
        while queue:
            size=len(queue)
            for i in range(size):
                element=queue.popleft()
                element.left,element.right=element.right,element.left
                if element.left is not None:
                    queue.append(element.left)
                if element.right is not None:
                    queue.append(element.right)
        return root
            
                
                    
        
        