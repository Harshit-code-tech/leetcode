class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        row, col = 0, 0
        move = {"UP": (-1, 0), "DOWN": (1, 0), "LEFT": (0, -1), "RIGHT": (0, 1)}
        for command in commands:
            dr, dc = move[command]
            row += dr
            col += dc
        return row * n + col