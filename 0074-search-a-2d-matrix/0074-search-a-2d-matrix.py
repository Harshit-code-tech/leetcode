class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1

        while top <= bot:
            mid = (top + bot) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                break
            elif matrix[mid][0] > target:
                bot = mid - 1
            else:
                top = mid + 1
        else:
            # means we didn't find any valid row
            return False

        row = (top + bot) // 2
        left, right = 0, len(matrix[row]) - 1

        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False
