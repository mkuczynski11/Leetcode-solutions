#https://leetcode.com/problems/jump-game-ii/
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1: return 0
        l, r = 0, nums[0]
        i = 1
        while r < len(nums) - 1:
            i += 1
            l, r = r, max(k + nums[k] for k in range(l, r + 1))
        return i

a = Solution()
tab = [2,3,0,1,4]
print(a.jump(tab))