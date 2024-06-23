class Solution:
    def solve(self, dp: List[List[int]], nums: List[int], idx: int, flag: int) -> int:
        if idx < 0:
            return 0
        if idx == 0:
            if flag == 0:
                return nums[0]
            else:
                return -float('inf')
        if dp[idx][flag] != -1:
            return dp[idx][flag]
        
        ans = -float('inf')
        if flag == 0:
            ans = max(ans, nums[idx] + self.solve(dp, nums, idx - 1, 0))
            ans = max(ans, nums[idx] + self.solve(dp, nums, idx - 1, 1))
        else:
            ans = max(ans, -nums[idx] + self.solve(dp, nums, idx - 1, 0))
        
        dp[idx][flag] = ans
        return ans

    def maximumTotalCost(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1 for _ in range(2)] for _ in range(n)]
        return max(self.solve(dp, nums, n - 1, 0), self.solve(dp, nums, n - 1, 1))