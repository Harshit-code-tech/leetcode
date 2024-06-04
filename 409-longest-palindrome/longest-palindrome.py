class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = {}
        for i in s:
            char_count[i] = char_count.get(i, 0) + 1
        print(char_count) 

        length = 0
        even = 0
        odd = 0
        odd_flag = False

        for char in char_count:
            if char_count[char] % 2 == 0:
                length += char_count[char]
            else:
                length += char_count[char] - 1 
                odd_flag = True
        
        length += (1 if odd_flag else 0)

        # length = even + odd
        
        return length