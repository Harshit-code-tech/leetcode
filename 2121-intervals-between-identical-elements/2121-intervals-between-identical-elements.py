class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        group={}
        for i, num in enumerate(arr):
            if num not in group:
                group[num]=[]
            group[num].append(i)

        ans=[0]*len(arr)
        for indices in group.values():
            left_count,right_count,left_sum,right_sum=0,0,0,0
            for i in indices:
                ans[i]=(left_count*i)-left_sum
                left_count+=1
                left_sum+=i
            for i in reversed(indices):
                ans[i]+=right_sum-(right_count*i)
                right_count+=1
                right_sum+=i
        return ans
        