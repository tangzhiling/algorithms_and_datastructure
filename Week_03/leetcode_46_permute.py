"""

leetcode 46 :

Given an array nums of distinct integers, return all the possible 
permutations. You can return the answer in any order.

"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        self.dfs(nums, res, [])
        return res
        
    def dfs(self, nums, res, path):
        if not nums:
            res.append(path)
        else:
            for i in xrange(len(nums)):
                self.dfs(nums[:i] + nums[i + 1:], res, path + [nums[i]])