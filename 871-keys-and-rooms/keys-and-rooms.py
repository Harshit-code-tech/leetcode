
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if len(rooms[0])==0:
            return False
        v={0:1}
        l=[]
        l.extend(rooms[0])
        while l:
            m=l.pop(0)
            if m not in v:
                v[m]=1
                l.extend(rooms[m])
        if len(v)==len(rooms):
            return True
        return False