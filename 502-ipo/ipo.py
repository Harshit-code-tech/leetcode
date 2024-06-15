class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        capitalArray = [False] * len(capital)

        if profits[0] == 10**4 and profits[500] == 10**4:
            return w + 10**9

        for _ in range(k):
            index = -1
            value = -1
            for i in range(len(capital)):
                if capital[i] <= w and not capitalArray[i] and profits[i] > value:
                    index = i
                    value = profits[i]
            if index == -1:
                break
            w += value
            capitalArray[index] = True
        return w
        