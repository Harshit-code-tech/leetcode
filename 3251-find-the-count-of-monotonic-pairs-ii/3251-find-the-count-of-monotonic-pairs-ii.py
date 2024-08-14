class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        max_val = max(nums)     
        dp = [1] * (max_val + 1)        
        for i in range(1, n):
            d = max(0, nums[i] - nums[i - 1])
            prefix_sum = [0] * (max_val + 1)
            prefix_sum[0] = dp[0]
            for j in range(1, max_val + 1):
                prefix_sum[j] = (prefix_sum[j-1] + dp[j]) % MOD
            dp2 = [(prefix_sum[j - d] if j >= d else 0) for j in range(nums[i] + 1)]
            dp = dp2 + [0] * (max_val - nums[i] + 1)  
        return sum(dp[:nums[-1] + 1]) % MOD