#https://leetcode.com/problems/zigzag-conversion/
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if(numRows == 1): return s
        result = ''
        top = 0
        bot = numRows - 1
        start = 0
        while bot >= 0:
            c = start
            i = 0
            while c < len(s):
                result += s[c]
                i += 1
                if(i%2 == 1 and bot != 0):
                    c += 2 * bot
                elif(i%2 == 0 and top != 0):
                    c += 2 * top
                else:
                    c += 2*top + 2*bot
            start += 1
            top += 1
            bot -= 1
        return result