class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        n = len(s)
        cycle = 2*numRows - 2
        strlist = []
        for i in range(numRows):
            for j in range(i, n, cycle):
                strlist.append(s[j])
                print (j,j+cycle-2*i)
                if i != numRows-1 and i != 0 and j+cycle-2*i < n:
                    strlist.append(s[j+cycle-2*i])
        newstr = ''.join(strlist)
        return newstr

if __name__=="__main__":
    ip1 = input("Enter the string!!")
    ip2 = int(input("Enter number of rows"))
    s = Solution()
    print(s.convert(ip1,ip2))
