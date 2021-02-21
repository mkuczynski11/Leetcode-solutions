#https://leetcode.com/problems/unique-paths/
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        tab = [[1 for _ in range(n)]for _ in range(m)] 
        for i in range(m-2, -1,-1):                     
            for j in range(n-2, -1, -1):                
                tab[i][j] = tab[i+1][j] + tab[i][j+1]
        return tab[0][0]

a = Solution()
print(a.uniquePaths(3,7))