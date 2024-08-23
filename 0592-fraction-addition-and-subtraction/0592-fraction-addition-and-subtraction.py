import re
from math import gcd


class Solution:
    def fractionAddition(self, expression: str) -> str:
            
        fractions = re.findall('[+-]?\\d+/\\d+', expression)
        print(fractions)
    
        num, denom = 0, 1
        
        for fraction in fractions:
            n, d = map(int, fraction.split('/'))
            print(n,d)
    
            num = num * d + n * denom
            denom = denom * d
            
            g = gcd(abs(num), denom)
            num = num // g
            denom = denom // g
        
        if denom < 0:
            num = -num
            denom = -denom
        
        return f"{num}/{denom}"