class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        dp = [[0] * 51 for _ in range(n)]
        for j in range(nums[0] + 1):
            dp[0][j] = 1

        for i in range(1, n):
            for j in range(nums[i] + 1):
                for k in range(j + 1):
                    if nums[i] - j <= nums[i-1] - k:
                        dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD
        result = sum(dp[-1]) % MOD
        return result

