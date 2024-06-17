class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()

        ans = []

        for i in range(len(spells)):
            amt = success/spells[i]
            idx = bisect_left(potions,amt)
            ans.append(len(potions)-idx)

        return ans