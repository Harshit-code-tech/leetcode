class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        #getting binary representation of every number
        c = str(bin(c)[2:])
        a = str(bin(a)[2:])
        b = str(bin(b)[2:])

        #checking if all have equal length
        d = max([a,b,c],key = len)
        x = len(d)-len(b)
        y = len(d)-len(a)
        z = len(d)-len(c)

        #adding additional zeroes if there a difference in length
        while x>0:
            b = '0'+b
            x -= 1
        while y>0:
            a = '0'+a
            y -= 1
        while z>0:
            c = '0'+c
            z -= 1

        #checking all four possible cases of bitwise OR
        co = 0
        for x in range(len(a)):
            if a[x]=='1' and b[x] == '1' and c[x]!='1':
                co += 2
            elif a[x]=='0' and b[x]=='0' and c[x]!='0':
                co += 1
            elif a[x]=='0' and b[x]=='1' and c[x]!='1':
                co += 1
            elif a[x]=='1' and b[x]=='0' and c[x]!='1':
                co += 1

        return co