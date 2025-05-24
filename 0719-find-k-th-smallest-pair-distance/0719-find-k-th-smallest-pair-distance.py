class Solution:
    def smallestDistancePair(self, arr: List[int], k: int) -> int:
            arr.sort()
            n = len(arr)
            left, right = 0, arr[-1] - arr[0]
            
            while left < right:
                mid = (left + right) // 2
                count = 0
                j = 0
                
                for i in range(n):
                    while j < n and arr[j] - arr[i] <= mid:
                        j += 1
                    count += j - i - 1
                
                if count < k:
                    left = mid + 1
                else:
                    right = mid
                    
            return left