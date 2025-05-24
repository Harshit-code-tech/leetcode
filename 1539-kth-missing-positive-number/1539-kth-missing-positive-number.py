class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing=0
        current=1
        index=0
        while missing < k:
            if index < len(arr) and arr[index] == current:
                index += 1
            else:
                missing += 1
                if missing == k:
                    return current
            current += 1
        
        return -1 

        