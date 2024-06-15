class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        n = len(equations)
        graph = defaultdict(dict)
        for idx, (src, dest) in enumerate(equations):
            graph[src][dest] = values[idx]
            graph[dest][src] = 1/values[idx]

        def dfs(src, dest, res):
            if src not in graph or dest not in graph or src in visited:
                return -1
            if src == dest:
                return res
            visited.add(src)
            for nei, val in graph[src].items():
                temp = dfs(nei, dest, res * val)
                if temp != -1:
                    return temp
            return -1
        result = []
        for src, dest in queries:
            visited = set()
            val = dfs(src, dest, 1)
            result.append(val)
            
        return result