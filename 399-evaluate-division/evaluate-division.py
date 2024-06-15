class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        for (A, B), value in zip(equations, values):
            graph[A][B] = value
            graph[B][A] = 1.0/value

        def findPath(C, D) -> float:
            if C not in graph or D not in graph:
                return -1
            
            if C == D:
                return 1
            
            stack = [(C, 1)]
            visited = set()

            while(stack):
                (nodeLabel, value) = stack.pop()
                visited.add(nodeLabel)

                if (nodeLabel == D):
                    return value

                for neighbor in graph[nodeLabel].items():
                    if (neighbor[0] not in visited):
                        stack.append((neighbor[0], value * neighbor[1]))
            
            return -1

        result = []

        for (C, D) in queries:
            result.append(findPath(C, D))
        
        return result
        