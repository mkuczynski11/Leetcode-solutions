#https://leetcode.com/problems/generate-parentheses/
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        '''
        i = 1
        s = '()'
        mySet = set([s])
        addSet = set()
        removeSet = set()
        while i < n:
            for x in mySet:
                removeSet.add(x)
                j = 0
                while j < len(x):
                    res = x[0:j] + s + x[j:]
                    addSet.add(res)
                    j+=1
            i+=1
            for x in addSet:
                mySet.add(x)
            for x in removeSet:
                mySet.discard(x)
        return mySet
        '''
        res = []
        def mutate(s, l, r):
            if len(s) == 2*n:
                res.append(s)
            if l < n:
                mutate(s+'(',l+1 , r)
            if r < l:
                mutate(s+')',l, r+1)
        mutate('',0,0)
        return res

a = Solution()
print(a.generateParenthesis(3))