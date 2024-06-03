class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i,j=0,0
        for ch in s:
            if ch == t[j]:
                i += 1
                j += 1
                if j == len(t):
                    return 0      
        return len(t) - i
