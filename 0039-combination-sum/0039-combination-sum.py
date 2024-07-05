class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.backtrack(candidates, 0, [], target, result)
        return result

    def backtrack(self, candidates: List[int], start: int, curr: List[int], target: int, result: List[List[int]]):
        if target == 0:
            result.append(curr.copy()) 
            return

        for i in range(start, len(candidates)):
            if candidates[i] <= target:
                curr.append(candidates[i])
                self.backtrack(candidates, i, curr, target - candidates[i], result)
                curr.pop()

