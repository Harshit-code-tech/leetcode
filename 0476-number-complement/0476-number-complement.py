class Solution(object):
    def findComplement(self, num):
        bin1=bin(num)
        bin11=bin1[2:]
        bin12=''
        for i in bin11:
            if i=='1':
                bin12+='0'
            else:
                bin12+='1'
        final=int(bin12,2)
        return final
