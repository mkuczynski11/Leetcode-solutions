class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #float('inf')
        #float('-inf')
        max_int = (pow(2,31)-1).__str__()
        min_int = (-1*pow(2,31)).__str__()
        y = x.__str__()[::-1]
        if(y[-1] == '-'):
            y = y[:len(y) - 1]
            y = '-' + y
        if(len(y) == 11 or len(y) == 10):
            i = 0
            check = 0
            if(len(y) == 10 and y[0] == '-'): return int(y)
            elif(len(y) == 11): i = 1; check = min_int
            elif(len(y) == 10): i = 0; check = max_int

            while i < len(y):
                if(int(y[i]) > int(check[i])):
                    return 0
                elif(int(y[i]) < int(check[i])):
                    break
                i += 1
        return int(y)

a = Solution()
print(a.reverse(1534236469))