class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        last=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[last]=nums[i]
                last+=1
        for i in range (last,len(nums)):
            nums[i]=0