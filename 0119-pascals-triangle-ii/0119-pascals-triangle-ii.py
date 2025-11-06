def nCr(n, r):
    res = 1
    for i in range(r):
        res = res * (n - i) // (i + 1)
    return res

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return [nCr(rowIndex, k) for k in range(rowIndex + 1)]
