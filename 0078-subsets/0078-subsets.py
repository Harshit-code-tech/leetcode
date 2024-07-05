class Solution(object):
    def subsets(self, nums):
        res  = []
        sol = []
        def dfs(i):
            if(len(nums)) <= i:
                res.append(sol[:])
                return
            sol.append(nums[i])
            dfs(i+1)
            sol.pop()
            dfs(i+1)
        dfs(0)
        return(res)