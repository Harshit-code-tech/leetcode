class Solution:
    def reverse(self, arr: List[int], start: int, end: int) -> None:
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    def rotate(self, arr: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(arr)
        k = k % n  
        self.reverse(arr, 0, n - 1)
        self.reverse(arr, 0, k - 1)
        self.reverse(arr, k, n - 1)