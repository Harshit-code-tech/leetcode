class Solution:
    def calculate(self, s: str) -> int:
        total = num = 0
        sign = 1
        stack = []

        for ch in s.replace(" ", ""):
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch in '+-':
                total += sign * num
                num, sign = 0, 1 if ch == '+' else -1
            elif ch == '(':
                stack.append((total, sign))
                total, sign, num = 0, 1, 0
            elif ch == ')':
                total += sign * num
                prev_total, prev_sign = stack.pop()
                total = prev_total + prev_sign * total
                num = 0

        return total + sign * num
