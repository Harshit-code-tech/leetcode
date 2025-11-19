class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # total_len=len(nums)
        # arr=list(set(nums))
        # count=0
        # for i,num in enumerate(arr):
        #     count+=1
        # left=["_"]*(total_len-len(arr))
        
        # arr.extend(left)

        # return count,arr[for count in arr]
        if not nums:
            return 0

        i=0
        for j in range(1,len(nums)):
            if nums[j]!=nums[i]:
                i+=1
                nums[i]=nums[j]

        return i+1



