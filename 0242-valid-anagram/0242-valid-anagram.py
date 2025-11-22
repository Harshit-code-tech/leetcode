class Solution:
    def isAnagram(self, s: str, t: str) -> bool: 
        if len(s)!=len(t):
            return False

        char_st={}
        for char in s:
            if char in char_st:
                char_st[char]+=1
            char_st[char]=1
        for char in t:
            if char in char_st:
                char_st[char]-=1
            char_st[char]=-1
        for val in char_st.values():
            if val<0:
                return False
            return True
        # if len(s) != len(t):
        #     return False

        # count_t={}
        # count_s={}

        # for char in s:
        #     if char in count_s:
        #         count_s[char]+=1
        #     else:
        #         count_s[char]=1

        # for char1 in t:
        #     if char1 in count_t:
        #         count_t[char1]+=1
        #     else:
        #         count_t[char1]=1

        # if count_s!=count_t:
        #     return False
        # return True
            
 