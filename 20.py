#https://leetcode.com/problems/valid-parentheses/
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        q = []
        bracketsMap = {"(":")", "[":"]", "{": "}"}
        openBrackets = set(["(","[","{"])
        for c in s:
            if c in openBrackets: q.append(c)
            elif q and c == bracketsMap[q[-1]]:
                q.pop()
            else:
                return False

        return q == []

a = Solution()
print(a.isValid("("))