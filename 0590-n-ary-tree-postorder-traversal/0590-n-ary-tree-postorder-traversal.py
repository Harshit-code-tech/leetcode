class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if visited:
                res.append(node.val)
            else:
                stack.append((node, True))
                for c in node.children[::-1]:
                    stack.append((c, False))
        return res