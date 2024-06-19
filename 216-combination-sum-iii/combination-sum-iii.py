class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def dfs(start, path, currSum):
            if len(path)==k and currSum==n:
                res.append(path)
                return
            elif (len(path)==k and currSum!=n):
                return
            for i in range(start, 10):
                dfs(i+1, path+[i], currSum+i)

        dfs(1, [], 0)
        return res



        