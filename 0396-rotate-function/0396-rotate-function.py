class Solution:
    def maxRotateFunction(self, arr: List[int]) -> int:
        n = len(arr)
        total_sum = 0
        curr_f = 0
        
        for i in range(n):
            total_sum += arr[i]
            curr_f += i * arr[i]
        
        max_f = curr_f
        
        for i in range(1, n):
            curr_f += total_sum - n * arr[n - i]
            if curr_f > max_f:
                max_f = curr_f
        
        return max_f