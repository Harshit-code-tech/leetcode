class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m,n=entrance; queue=[(m,n)]; ans=0; seen=set(); seen.add((m,n))
        while queue:
            for _ in range(len(queue)):
                x,y=queue.pop(0)
            
                for dx,dy in ((-1,0),(0,-1),(0,1),(1,0)):
                    p=x+dx; q=y+dy
                
                    if 0<=p<len(maze) and 0<=q<len(maze[0]) and maze[p][q]=="." and (p,q) not in seen:
                        queue.append((p,q))
                        seen.add((p,q))
                    
                        if (p==0 or p==len(maze)-1 or q==0 or q==len(maze[0])-1) :
                            return ans+1      
            ans+=1
        return -1
        