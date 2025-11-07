class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        freq_t = {}
        for ch in t:
            freq_t[ch] = freq_t.get(ch, 0) + 1

        freq_s = {}
        left = 0
        min_len = float("inf")
        min_sub = ""

        for right in range(len(s)):
            ch = s[right]
            freq_s[ch] = freq_s.get(ch, 0) + 1

            # check if window has all required chars
            def has_all():
                for k in freq_t:
                    if freq_s.get(k, 0) < freq_t[k]:
                        return False
                return True

            while has_all() and left <= right:
                curr_len = right - left + 1
                if curr_len < min_len:
                    min_len = curr_len
                    min_sub = s[left:right+1]
                freq_s[s[left]] -= 1
                left += 1

        return min_sub