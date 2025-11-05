class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        
        if n1 > n2:
            return False
        freq1 = [0] * 26
        for ch in s1:
            freq1[ord(ch) - ord('a')] += 1
        freq2 = [0] * 26
        for i in range(n1):
            freq2[ord(s2[i]) - ord('a')] += 1
        if freq1 == freq2:
            return True
        for right in range(n1, n2):
            freq2[ord(s2[right]) - ord('a')] += 1
            left_char_index = ord(s2[right - n1]) - ord('a')
            freq2[left_char_index] -= 1
            if freq1==freq2:
                return True
        
        return False
