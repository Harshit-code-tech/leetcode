# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        queue = []
        queue.append(root)
        most_right = []
        while len(queue) > 0:
            n = len(queue)
            most_right.append(queue[-1].val)
            for i in range(n):
                element = queue.pop(0)
                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)
        return most_right