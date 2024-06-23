class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count_rem1=0
        count_rem2=0
        for num in nums:
            r=num%3
            if r==1:
                count_rem1+=1
            elif r==2:
                count_rem2+=1
        return count_rem1+count_rem2
        