class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        # 2nd Pass: Validation
        if nums.count(candidate) > len(nums) // 2:
            return candidate
        return -1  # or None, if no majority element