#https://leetcode.com/problems/minimum-path-sum/
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        w = len(grid[0])-1
        h = len(grid)-1
        for i in range(h, -1 , -1):
            for j in range(w, -1 , -1):
                a = b = 0
                if(i == h):
                    a = float('inf')
                else:
                    a = grid[i+1][j]
                if(j == w):
                    b = float('inf')
                else:
                    b = grid[i][j+1]
                grid[i][j] = grid[i][j] if a==float('inf') and b == float('inf') else min(a,b)+grid[i][j]

        return grid[0][0]
a = Solution()
tab = [[1,3,1],[1,5,1],[4,2,1]]
print(a.minPathSum(tab))