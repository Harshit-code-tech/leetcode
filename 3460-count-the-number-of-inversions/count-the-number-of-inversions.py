MOD = 10**9 + 7

class Solution:
    def __init__(self):
        self.dp = None
    
    def numberOfPermutations(self, n, requirements):
        self.dp = [[None] * (n * (n - 1) // 2 + 1) for _ in range(n + 1)]
        
        # Sort requirements by position
        requirements.sort(key=lambda x: x[0])
        
        # Process each requirement
        for r in requirements:
            pos, inv = r[0], r[1]
            if self.count(pos, inv) == 0:
                return 0
            # Enforce the current requirement
            for i in range(len(self.dp[pos])):
                if i != inv:
                    self.dp[pos][i] = 0
        
        # Return the result based on the last requirement
        last = requirements[-1]
        return self.dp[last[0]][last[1]]
    
    def count(self, pos, inv):
        if inv < 0:
            return 0
        if pos == 0:
            return 1 if inv == 0 else 0
        if self.dp[pos][inv] is not None:
            return self.dp[pos][inv]
        res = 0
        for i in range(pos + 1):
            res = (res + self.count(pos - 1, inv - i)) % MOD
        self.dp[pos][inv] = res
        return res