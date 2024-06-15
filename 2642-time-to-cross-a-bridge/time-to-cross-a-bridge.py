class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        left_warehouse, left_bridge, right_warehouse, right_bridge = [], [], [], []
        curr_time = 0
        #initially everyone is in front of the left bridge
        for i in range(k):
            heapq.heappush(left_bridge,(-time[i][0]-time[i][2], -i))
        #return the loop till we have boxes / there is someone on the right back of the river who needs to come back
        while n or right_warehouse or right_bridge:
            #we need to move the workers to the bridge edges before starting any movement
            while left_warehouse and left_warehouse[0][0] <= curr_time:
                _, i = heapq.heappop(left_warehouse)
                heapq.heappush(left_bridge,(-time[i][0]-time[i][2], -i))
            while right_warehouse and right_warehouse[0][0] <= curr_time:
                _, i = heapq.heappop(right_warehouse)
                heapq.heappush(right_bridge,(-time[i][0]-time[i][2], -i))
            #workers on right end move to the left end
            if right_bridge:
                _, i = heapq.heappop(right_bridge)
                l, po, r, pn = time[-i]
                curr_time += r
                heapq.heappush(left_warehouse,(curr_time+pn, -i))
                n -= 1
            #if there are more boxes in right and fewer workers, we need to move additional workers from the left
            elif left_bridge and n > len(right_warehouse) + len(right_bridge):
                _, i = heapq.heappop(left_bridge)
                l, po, r, pn = time[-i]
                curr_time += l
                heapq.heappush(right_warehouse,(curr_time+po, -i))
            #if there are no workers on the left end of the bridge and there are boxes 
            #OR
            #if there are workers on the left end but no boxes 
            else:
                left_time = left_warehouse[0][0] if left_warehouse and n > len(right_warehouse) + len(right_bridge) else math.inf
                right_time = right_warehouse[0][0] if right_warehouse else math.inf
                curr_time = min(left_time,right_time)
        return curr_time                    