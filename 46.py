#https://leetcode.com/problems/permutations/
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []
        self.permuteHelper(nums, [], result, len(nums))
        return result

    
    def permuteHelper(self,nums, current, result, l):
        if len(current) == l:
            result.append(current)
            return
        for i in range(len(nums)):
            self.permuteHelper(nums[:i]+nums[i+1:],current+[nums[i]],result,l)
        return


a = Solution()
tab = []
print(a.permute(tab))