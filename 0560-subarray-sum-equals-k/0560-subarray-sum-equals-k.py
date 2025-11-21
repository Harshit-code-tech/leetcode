class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        curr_sum=0
        seen_sum={0:1}
        for num in nums:
            curr_sum+=num
            target=curr_sum-k

            if target in seen_sum:
                count += seen_sum[target]
            seen_sum[curr_sum] = seen_sum.get(curr_sum, 0) + 1
        return count

        

