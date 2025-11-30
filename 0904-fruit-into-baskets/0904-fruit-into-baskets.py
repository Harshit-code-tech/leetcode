class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        seen={}
        left=0
        ans=0
        for right,fruit in enumerate(fruits):
            seen[fruit]=seen.get(fruit,0)+1
            while len(seen)>2:
                lfruit=fruits[left]
                seen[lfruit] -=1
                if seen[lfruit]==0:
                    seen.pop(lfruit)
                left+=1
            ans=max(ans,right-left+1)
        return ans


        