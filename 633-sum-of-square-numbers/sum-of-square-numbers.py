class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        return any(b == int(b) for b in (sqrt(c - a * a) for a in range(int(sqrt(c)) + 1)))


