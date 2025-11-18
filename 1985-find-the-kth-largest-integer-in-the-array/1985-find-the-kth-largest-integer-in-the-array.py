class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        # unque=list(set(nums))
        nums.sort(key=int)
        if len(nums)<k:
            return ""

        return nums[-k]
        