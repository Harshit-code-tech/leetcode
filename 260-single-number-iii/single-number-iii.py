class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_all = 0
        for num in nums:
            xor_all ^= num

        set_bit = xor_all & -xor_all
        a, b = 0, 0

        for num in nums:
            if num & set_bit:
                a ^= num
            else:
                b ^= num

        return [a, b]