class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        count = 0
        r_map = {}      
        for hour in hours:
            reminder = hour % 24
            c = (24 - reminder) % 24         
            if c in r_map:
                count += r_map[c]              
            if reminder in r_map:
                r_map[reminder] += 1
            else:
                r_map[reminder] = 1                
        return count
