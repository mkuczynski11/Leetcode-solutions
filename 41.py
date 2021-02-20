#https://leetcode.com/problems/first-missing-positive/
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)):
            if(nums[i] >= len(nums) or nums[i] < 0):
                nums[i] = 0
        for i in range(len(nums)):
            nums[nums[i]%n] += n
        for i in range(len(nums)):
            if(nums[i]//n == 0): return i
        return n

a = Solution()
tab = [3,4,-1,1]
print(a.firstMissingPositive(tab))