class Solution:
    from functools import lru_cache
    def rob(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dp(i):
            if i >=len(nums):
                return 0

            take=nums[i]+dp(i+2)
            leave=dp(i+1)
            return max(take,leave)
        return dp(0)

        