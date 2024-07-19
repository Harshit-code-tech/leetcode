class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        minimum = []
        maximum = []

        for i in range(len(matrix)):
            minimum.append(min(matrix[i]))

        for j in range(len(matrix[0])):
           col_max = max(matrix[i][j] for i in range(len(matrix)))
           maximum.append(col_max)

        result = []
        for num in minimum:
            if num in maximum:
                result.append(num)

        return result