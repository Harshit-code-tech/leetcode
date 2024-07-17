# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        stack = [(root, True)]
        delete = set(to_delete)
        res = []
        while stack:
            node, canAdd = stack.pop()
            if canAdd and node.val not in delete:
                res.append(node)
                canAdd = False
            if node.left:
                if node.left.val in delete:
                    stack.append((node.left,True))
                    node.left = None
                else:
                    stack.append((node.left, canAdd))
            if node.right:
                if node.right.val in delete:
                    stack.append((node.right,True))
                    node.right = None
                else:
                    stack.append((node.right, canAdd))
        return res

                
