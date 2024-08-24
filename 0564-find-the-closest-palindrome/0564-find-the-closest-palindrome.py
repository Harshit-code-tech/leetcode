class Solution:
    def nearestPalindromic(self, n: str) -> str:
        # Edge case for single-digit numbers
        if n == "1":
            return "0"

        num_len = len(n)
        num = int(n)

        # Generate candidate palindromes by manipulating the prefix
        candidates = set()
        
        # Case 1: Just smaller palindrome
        smaller_half = int(n[:(num_len + 1) // 2]) - 1
        candidates.add(self.create_palindrome(smaller_half, num_len))
        
        # Case 2: Exact palindrome from prefix
        exact_half = int(n[:(num_len + 1) // 2])
        candidates.add(self.create_palindrome(exact_half, num_len))
        
        # Case 3: Just larger palindrome
        larger_half = int(n[:(num_len + 1) // 2]) + 1
        candidates.add(self.create_palindrome(larger_half, num_len))

        # Adding two edge cases: '999...999' and '1000...0001'
        candidates.add(str(10**num_len + 1))  # Next higher of the form 1000...0001
        candidates.add(str(10**(num_len - 1) - 1))  # Next lower of the form 999...999
        
        # Remove the number itself if present
        candidates.discard(n)
        
        # Find the closest palindrome
        return min(candidates, key=lambda x: (abs(int(x) - num), int(x)))

    def create_palindrome(self, half: int, length: int) -> str:
        half_str = str(half)
        if length % 2 == 0:
            return half_str + half_str[::-1]  # Even length palindrome
        else:
            return half_str + half_str[:-1][::-1]  # Odd length palindrome