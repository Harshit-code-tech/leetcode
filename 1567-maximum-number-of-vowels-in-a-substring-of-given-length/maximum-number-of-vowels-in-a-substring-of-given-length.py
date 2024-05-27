class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        max_vowels = curr_vowels = sum([1 for c in s[:k] if c in vowels])
        for i in range(len(s) - k):
            curr_vowels += (s[i+k] in vowels) - (s[i] in vowels)
            if curr_vowels > max_vowels:
                max_vowels = curr_vowels
        return max_vowels