class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0        
        op = 0
        curr = 1        
        for num in nums:
            if num != curr:
                op += 1
                curr = 1 - curr                
        return op
        