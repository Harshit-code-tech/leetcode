class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        left=0
        s=0
        ans=float('inf')
        for right in range(len(nums)):
            s+=nums[right]
            while s>=target:
                ans=min(ans,right-left+1)
                s-=nums[left]
                left+=1
        return ans if ans!=float('inf') else 0