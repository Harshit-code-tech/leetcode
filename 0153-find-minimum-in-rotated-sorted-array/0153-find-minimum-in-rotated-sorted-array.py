class Solution:
    def is_sorted(self, nums):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False
        return True
    
    def rotate_left(self, nums):
        if len(nums) == 0:
            return nums
        first = nums[0]
        for i in range(1, len(nums)):
            nums[i - 1] = nums[i]
        nums[-1] = first
        return nums
    def make_sorted(self, nums):
        for _ in range(len(nums)):
            if self.is_sorted(nums):
                return nums
            nums = self.rotate_left(nums)
        return nums

    
    def findMin(self, nums: List[int]) -> int:
        nums = self.make_sorted(nums)

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]