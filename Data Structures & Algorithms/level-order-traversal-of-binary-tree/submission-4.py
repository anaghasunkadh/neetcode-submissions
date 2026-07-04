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
        queue=collections.deque()
        levels=[]
        queue.append(root)
        while queue:
            value=[]
            leng=len(queue)
            for i in range(leng):
                element=queue.popleft()
                value.append(element.val)
                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)
            levels.append(value)
        return levels


        