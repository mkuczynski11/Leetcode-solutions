#https://leetcode.com/problems/combination-sum/
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        '''
        result = []
        sums = []
        candidates.sort()
        for x in candidates:
            if target-x > 0:
                sums.append([target - x,[x]])
            elif target - x == 0:
                result.append([x])
            else:
                break
        if not sums and not result: return []
        while True:
            if(len(sums) == 0): break
            for x in candidates:
                if(sums[0][0] - x) > 0:
                    sums.append([sums[0][0] - x,sums[0][1]+[x]])
                elif(sums[0][0] - x) == 0:
                    sums[0][1].append(x)
                    sums[0][1].sort()
                    if(sums[0][1] not in result):
                        result.append(sums[0][1])
                else:
                    break
            sums.pop(0)
        return result
        '''
        result = []
        self.dfs(candidates,target, [], result)
        return result

    def dfs(self, nums, target, path, result):
        if target < 0:
            return
        if target == 0:
            result.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[i:],target - nums[i],path+[nums[i]], result)



a = Solution()
tab = [2,7,6,3,5,1]
tar = 9
print(a.combinationSum(tab,tar))