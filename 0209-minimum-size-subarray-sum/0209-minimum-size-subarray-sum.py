class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)


        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        def binary_search(left: int, right: int, value: int) -> int:
            while left < right:
                mid = (left + right) // 2
                if prefix[mid] < value:
                    left = mid + 1
                else:
                    right = mid
            return left

        min_len = float('inf')
        for i in range(n):
            desired = prefix[i] + target
            bound = binary_search(i + 1, n + 1, desired)
            if bound <= n:
                min_len = min(min_len, bound - i)

        return min_len if min_len != float('inf') else 0