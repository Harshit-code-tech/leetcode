class Solution(object):
    def beautifulSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def dfs(idx, subset):
            if idx == len(nums): return bool(subset)
            if not any(abs(nums[idx] - x) == k for x in subset):
                return dfs(idx + 1, subset + [nums[idx]]) + dfs(idx + 1, subset)
            return dfs(idx + 1, subset)
        return dfs(0, [])