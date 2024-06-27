class Solution:
    def partitionString(self, s: str) -> int:
        st = set(())
        ans = 0
        for i in range(len(s)):
            if s[i] in st:
                st.clear()
                ans += 1
            st.add(s[i])
        ans += 1
        return ans