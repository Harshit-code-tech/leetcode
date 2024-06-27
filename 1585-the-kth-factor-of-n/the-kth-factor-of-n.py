class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors=[]
        for i in range(1,int(n**0.5)+1):
            if n%i==0:
                factors.append(i)
                if i*i !=n:
                    factors.append(n//i)
        factors.sort()
        if len(factors)<k:
            return -1
        else:
            return factors[k-1]
        