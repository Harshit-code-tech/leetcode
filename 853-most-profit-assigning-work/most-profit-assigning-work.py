class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(list(zip(difficulty, profit)), key=lambda x: (x[0], x[1]))
        
        worker.sort()
        res, i, max_profit = 0, 0, 0
        for skill in worker:
            while i < len(jobs):
                if jobs[i][0] > skill:
                    break
                max_profit = max(max_profit, jobs[i][1])
                i += 1
            res += max_profit
        return res