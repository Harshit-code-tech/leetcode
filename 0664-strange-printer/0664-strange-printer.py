class Solution:
    def strangePrinter(self, s: str) -> int:
        s = ''.join(char for char,_ in itertools.groupby(s))
        memo = {}
        def _minimum_steps(start,end):
            if start>end :  return 0
            if (start,end) in memo : return memo[(start,end)]
            min_steps = 1 + _minimum_steps(start+1,end)
            for k in range(start+1,end+1):
                if s[k] == s[start] :
                    steps = _minimum_steps(start,k-1) + _minimum_steps(k+1,end)
                    min_steps = min(min_steps,steps)
            memo[(start,end)] = min_steps
            return min_steps
        return _minimum_steps(0,len(s)-1)