#https://leetcode.com/problems/longest-valid-parentheses/
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        i = 0
        j = 0
        result = 0
        for c in s:
            if c == '(':
                i+=1
            else:
                j+=1
            if(i == j):
                if(i*2 > result): result = i*2
            elif(j >= i):
                i = 0
                j = 0
        i = j = 0
        for c in range(len(s)-1,-1,-1):
            if s[c] == '(':
                i += 1
            else:
                j += 1
            if (i == j):
                if(i*2 > result): result = i*2
            elif(i >= j):
                i = j = 0
        return result
        '''
        result = 0
        stack = []
        stack.append(-1)
        i = 0
        for c in s:
            if(c == '('):
                stack.append(i)
            else:
                stack.pop()
                if(len(stack) == 0):
                    stack.append(i)
                else:
                    result = max(result, i - stack[len(stack)-1])
            i+=1
        return result

a = Solution()
s = "(()"
print(a.longestValidParentheses(s))