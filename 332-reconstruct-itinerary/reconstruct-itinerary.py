class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()

        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src] += [dst]

        res = []
        stack = ['JFK']              

        while stack:
            last = stack[-1]
            if not graph[last]:
                res += [last]
                stack.pop()
            else:
                neigh = graph[last].pop(0)
                stack.append(neigh)
        return res[::-1]