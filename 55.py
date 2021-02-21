#https://leetcode.com/problems/jump-game/
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''
        l = 0
        r = nums[0]
        while r < len(nums)-1:
            l, r = r, max(k + nums[k] for k in range(l,r+1,1))
            if(l == r): return False
        return True
        '''
        i = len(nums)-1
        for j in range(i,-1,-1):
            if(j + nums[j] >= i):
                i =j 
        return i == 0

a = Solution()
tab = [3,2,1,0,4]
print(a.canJump(tab))