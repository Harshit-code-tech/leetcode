class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        total = 0
        num = 0
        sign = 1    
        stack = []  

        i = 0
        n = len(s)
        while i < n:
            ch = s[i]

            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == '+':
                total += sign * num
                num = 0
                sign = 1

            elif ch == '-':
                total += sign * num
                num = 0
                sign = -1

            elif ch == '(':
                stack.append(total)
                stack.append(sign)
                total = 0
                num = 0
                sign = 1

            elif ch == ')':
                total += sign * num
                num = 0
                prev_sign = stack.pop()
                prev_total = stack.pop()
                total = prev_total + prev_sign * total
            i += 1

        total += sign * num
        return total
