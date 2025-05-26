class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        for i in range(n):
            val = abs(nums[i])
            if nums[val - 1] > 0:
                nums[val - 1] = -nums[val - 1]

        return [i + 1 for i in range(n) if nums[i] > 0]
