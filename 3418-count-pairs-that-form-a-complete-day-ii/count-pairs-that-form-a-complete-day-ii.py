class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        count=0
        r_map={}
        for hour in hours:
            r=hour%24
            c_r=(24-r)%24
            if c_r in r_map:
                count+=r_map[c_r]
            if r in r_map:
                r_map[r]+=1
            else:
                r_map[r]=1
        return count