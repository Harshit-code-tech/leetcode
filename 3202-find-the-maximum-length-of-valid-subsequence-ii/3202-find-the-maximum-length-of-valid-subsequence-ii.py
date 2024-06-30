class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[1] * k for _ in range(n)] 
        for i in range(n):
            for j in range(i):
                remainder = (nums[i] + nums[j]) % k
                dp[i][remainder] = max(dp[i][remainder], dp[j][remainder] + 1)
        max_length = 0
        for row in dp:
            for length in row:
                max_length = max(max_length, length)
        
        return max_length