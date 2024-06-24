class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # We can of course keep track of only the previous. And use only that for our memory.
        # Will use text 2 to iterate cols.
        if len(text2) > len(text1):
            temp = text2
            text2 = text1
            text1 = temp
        
        # Keep track of the shortest arr. (Which we forced to be at text2)
        COLS = len(text1)
        ROWS = len(text2)
        tab = [0] * (ROWS + 1)

        for col in range(COLS - 1, -1, -1):
            new_tab = tab[:]
            for row in range(ROWS - 1, -1, -1):
                if text1[col] == text2[row]:
                    new_tab[row] = tab[row + 1] + 1
                else:
                    new_tab[row] = max(new_tab[row + 1], tab[row])
            tab = new_tab
        return tab[0]