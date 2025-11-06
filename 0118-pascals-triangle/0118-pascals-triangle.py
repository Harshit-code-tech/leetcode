class Solution:
    def generate(self, numRows):
        result = []
        for n in range(numRows):
            row = []
            val = 1
            for r in range(n + 1):
                row.append(val)
                # next value in the row using nCr relation
                val = val * (n - r) // (r + 1)
            result.append(row)
        return result
