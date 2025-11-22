class Solution:
    def isAnagram(self, s: str, t: str) -> bool: 
        if len(s)!=len(t):
            return False

        count_t={}
        count_s={}
        for char in s:
            if char in count_s:
                count_s[char]+=1
            else:
                count_s[char]=1

        for char in t:
            if char in count_t:
                count_t[char]+=1
            else:
                count_t[char]=1

        if count_s!=count_t:
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
            
 