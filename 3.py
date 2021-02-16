class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp = ''
        length = 0
        for c in s:
            if c in tmp:
                if(length < len(tmp)):
                    length = len(tmp)
                tmp = tmp.split(c,1)[1]
                tmp += c
            else:
                tmp += c
        if length < len(tmp):
            length = len(tmp)
        return length

a = Solution()
print(a.lengthOfLongestSubstring("pwwkew"))