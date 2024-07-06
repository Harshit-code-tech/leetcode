class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        ans =1
        direction=1
        for  i in range(time):
            if direction == 1:
                ans+=1
            else:
                ans-=1
            if ans==1:
                direction=1
            if ans==n:
                direction=-1

        return ans 

        