class Solution(object):
    def buildMatrix(self, k, rowConditions, colConditions):
        def topological_sort(graph, in_degree):
            # Perform topological sort to find valid order
            queue = deque([node for node in range(1, k + 1) if in_degree[node] == 0])
            result = []
            
            while queue:
                node = queue.popleft()
                result.append(node)
                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
            
            return result if len(result) == k else []

        # Build graph and in-degrees for row conditions
        row_graph = defaultdict(list)
        row_in_degree = [0] * (k + 1)
        
        for above, below in rowConditions:
            row_graph[above].append(below)
            row_in_degree[below] += 1
        
        row_order = topological_sort(row_graph, row_in_degree)
        if not row_order:
            return []

        # Build graph and in-degrees for column conditions
        col_graph = defaultdict(list)
        col_in_degree = [0] * (k + 1)
        
        for left, right in colConditions:
            col_graph[left].append(right)
            col_in_degree[right] += 1
        
        col_order = topological_sort(col_graph, col_in_degree)
        if not col_order:
            return []
        
        # Create a mapping from value to its row and column positions
        pos = {val: (row_order.index(val), col_order.index(val)) for val in range(1, k + 1)}

        # Initialize the matrix with zeros
        matrix = [[0] * k for _ in range(k)]
        
        # Place the numbers in the matrix based on their positions
        for num in range(1, k + 1):
            row, col = pos[num]
            matrix[row][col] = num
        
        return matrix