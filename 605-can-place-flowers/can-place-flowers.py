class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        i = 0

        while i < len(flowerbed):
            if (flowerbed[i] == 0 and
                (i == 0 or flowerbed[i - 1] == 0) and
                (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)):
                count += 1
                i += 1  # Skip the next spot since we just planted a flower
            if count >= n:
                return True
            i += 1

        return False
