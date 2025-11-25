class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # stack=[]
        # while k>0:
                
        #     for num in nums :
        #         stack.append(num)
        #         if stack[-1]>stack[-2]:
        #             stack.pop()
        #             k-=1
        # return stack
        stack=[]
        for n in num:
            while k>0 and stack and stack[-1]>n:
                stack.pop()
                k-=1
            stack.append(n)
       
        if k>0:
            stack=stack[:-k]

        res="".join(stack)
        res=res.lstrip("0")
        return res if res else "0"