class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        moves=0
        prev=float('-inf')
        for num in nums:
            if num<=prev:
                inc=prev-num+1
                moves+=inc
                num+=inc
            prev=num
        return moves
