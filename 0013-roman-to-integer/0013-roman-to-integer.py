class Solution:
    def romanToInt(self, s: str) -> int:
        rm={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        res=0
        for i in range(len(s)):
            curr=rm[s[i]]
            next=0
            if i<len(s)-1:
                next=rm.get(s[i+1])
            if curr<next:
                res-=curr
            else:
                res+=curr
        return res

        