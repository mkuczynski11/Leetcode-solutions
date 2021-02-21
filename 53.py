#https://leetcode.com/problems/maximum-subarray/
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = tmp = nums[0]
        for i in range(1,len(nums),1):
            tmp = max(tmp+nums[i], nums[i])
            if(maximum < tmp): maximum = tmp
        return maximum
        
a = Solution()
tab = [1,2,-1,-2,2,1,-2,1]
print(a.maxSubArray(tab))