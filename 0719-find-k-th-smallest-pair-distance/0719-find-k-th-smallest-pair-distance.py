class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:

        def cnt_pair(dist):
            left, cnt = 0, 0
            for right in range(1, len(nums)):
                while nums[right] - nums[left] > dist:
                    left += 1
                cnt += right - left
            return cnt

        nums.sort()
        return bisect_left(range(nums[-1] - nums[0]), k, key = cnt_pair)