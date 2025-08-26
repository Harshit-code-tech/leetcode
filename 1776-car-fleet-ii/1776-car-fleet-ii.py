class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:        
        stack = [] 
        ans = [-1] * len(cars)
        for i in range(len(cars)-1,-1,-1):
            while stack and cars[i][1] <= cars[stack[-1]][1]: 
                stack.pop()

            while stack: 
                collision_t = (cars[stack[-1]][0] - cars[i][0]) / (cars[i][1] - cars[stack[-1]][1])

                if ans[stack[-1]] == -1 or collision_t <= ans[stack[-1]]:
                    ans[i] = collision_t
                    break
                stack.pop()
            stack.append(i)
        return ans