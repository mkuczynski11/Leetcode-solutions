def findPalindrome(s,left,right):
            while(right < len(s) and left >= 0 and s[left] == s[right]):
                left -= 1
                right += 1
            return right-left-1

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        start, end = 0, 0
        for i in range(len(s)):
            len1 = findPalindrome(s,i,i)
            len2 = findPalindrome(s,i,i+1)
            length = max(len1,len2)
            if(length > end - start):
                start = i - (length -1)/2
                end = i + length/2
        return s[int(start):int(end + 1)]