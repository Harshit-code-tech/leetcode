class Solution:
    def countValidSubsequence(self, nums: List[int]) -> int:
        counter_even_sum, counter_odd_sum, counter_even, counter_odd = 0, 1, 2, 3
        counters = [0, 0, 0, 0]
        parity_flags = [True, False]
        for num in nums:
            parity = num % 2
            if (parity == 1 and not parity_flags[counter_odd_sum]) or (parity == 0 and parity_flags[counter_odd_sum]):
                parity_flags[counter_odd_sum] = not parity_flags[counter_odd_sum]
                counters[counter_odd_sum] += 1
            
            if (parity == 1 and not parity_flags[counter_even_sum]) or (parity == 0 and parity_flags[counter_even_sum]):
                parity_flags[counter_even_sum] = not parity_flags[counter_even_sum]
                counters[counter_even_sum] += 1
            
            if parity == 1:
                counters[counter_odd] += 1
            if parity == 0:
                counters[counter_even] += 1

        return max(counters)

    def maximumLength(self, nums: List[int]) -> int:
        return self.countValidSubsequence(nums)