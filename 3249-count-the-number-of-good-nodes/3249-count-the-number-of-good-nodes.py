class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        tree = defaultdict(list)      
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        def dfs(node, parent):
            size = 1
            subtree_sizes = []
            for neighbor in tree[node]:
                if neighbor != parent:
                    subtree_size = dfs(neighbor, node)
                    subtree_sizes.append(subtree_size)
                    size += subtree_size
            
            if not subtree_sizes or len(set(subtree_sizes)) == 1:
                self.good_nodes += 1
            
            return size
        
        self.good_nodes = 0
        dfs(0, -1)
        return self.good_nodes