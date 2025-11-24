class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sort_t=intervals.sort()
        i=0
        count=0
        j=1
        while j<len(intervals):
            curr=intervals[i]
            next_in=intervals[j]
            cs=curr[0]
            ce=curr[1]
            ns=next_in[0]
            ne=next_in[1]
            if(ce<=ns):#no overlap
                i=j
                j+=1

            
            elif(ce<=ne):
                # overlapping
                j+=1
                count+=1
            
            elif(ce>ne):
                # overlap but privious
                i=j
                j+=1
                count+=1
                
        return count
        