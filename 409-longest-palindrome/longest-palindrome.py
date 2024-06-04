class Solution:
    def longestPalindrome(self, s: str) -> int:
        max = 0
        oddc = False

        for c in Counter(s).values():
            max += c // 2 * 2
            if c % 2 == 1:
                if not oddc:
                    oddc = True
                    max += 1 
        return max
        