class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        count=0
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        # return nums
        
        for j in range(0,len(nums)):
            if nums[j]!=0:
                nums[j],nums[count]=nums[count],nums[j]
                count+=1
        return nums

        

        

        