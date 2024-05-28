class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = [0]
        for i in range(len(gain)):
            alt.append(alt[i]+gain[i])
        return max(alt)