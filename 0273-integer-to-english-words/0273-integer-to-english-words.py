class Solution(object):
    def numberToWords(self, num):
        less_than_twenty = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        ten_places = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        if num == 0:
            return "Zero"

        def two_digit(num):
            if num < 20:
                return less_than_twenty[num]
            else:
                tens = num // 10
                ones = num % 10
                return ten_places[tens] + ('' if ones == 0 else ' ' + less_than_twenty[ones])

        def three_digit(num):
            if not num: return ''
            if not num//100: return two_digit(num)
            return less_than_twenty[num//100] + ' ' +'Hundred' + (' ' + two_digit(num%100) if num%100 else '')

        billion = num // 1000000000
        million = (num // 1000000) % 1000
        thousand = (num // 1000) % 1000
        hundred = num % 1000

        res = ''
        if billion:
            res += three_digit(billion) + ' Billion'
        
        if million:
            if res:
                res += ' '
            res += three_digit(million) + ' Million'
        
        if thousand:
            if res:
                res += ' '
            res += three_digit(thousand) + ' Thousand'
        
        if hundred:
            if res:
                res += ' '
            res += three_digit(hundred)

        return res.strip()