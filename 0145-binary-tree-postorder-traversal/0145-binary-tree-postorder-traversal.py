# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        l=[]
        def fun(root):
            if root==None:
                return []
            fun(root.left)
            fun(root.right)
            l.append(root.val)
        fun(root)
        return l