class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash = {5: 0, 10: 0, 20: 0}
        
        for n in bills:
            if n > 5:
                cash[5] -= 1
            if n > 10:
                bill = 10 if cash[10] > 0 else 5
                cash[bill] -= 10 // bill
                
            cash[n] += 1
            if cash[5] < 0:
                return False

        return True