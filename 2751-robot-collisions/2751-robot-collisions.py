class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        temp =[]
        for i in range(len(positions)):
            temp.append([positions[i],i])
        temp = sorted(temp)
        stack = []
        for i in range(len(positions)):
            ind = temp[i][1]
            if directions[ind]=='R':
                stack.append(['R',ind])
            else:
                flag = True
                while stack and stack[-1][0]=='R' :
                    
                    if healths[stack[-1][1]] == healths[ind]:
                        stack.pop()
                        flag = False
                        break
                    elif healths[stack[-1][1]] > healths[ind]:
                        healths[stack[-1][1]] -= 1
                        flag = False
                        break
                    else:
                        stack.pop()
                        healths[ind]-=1
                if  flag:
                    if healths[ind]>0:
                        stack.append(['L',ind])
        res = []
        stack = sorted(stack, key=lambda x:x[1])
        for i in stack:
            res.append(healths[i[1]])
        return res

                        
        

            