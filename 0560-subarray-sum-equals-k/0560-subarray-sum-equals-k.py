class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref_index = {0: -1}  # prefix sum 0 at index -1 (empty prefix)
        curr = 0
        best = 0

        for j, val in enumerate(nums):
            curr += val
            # if we haven't seen this prefix sum before, record earliest index
            if curr not in pref_index:
                pref_index[curr] = j
            # check if there's a prefix sum such that curr - prev = k -> prev = curr - k
            need = curr - k
            if need in pref_index:
                i = pref_index[need]
                length = j - i
                if length > best:
                    best = length
        return best
        

