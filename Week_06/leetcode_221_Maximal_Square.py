"""
leetcode 221. Maximal Square

Given an m x n binary matrix filled with 0's and 1's, find the 
largest square containing only 1's and return its area.


"""

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if not matrix: return 0
        res = 0
        row, col = len(matrix), len(matrix[0])

        dp = [[1 if matrix[i][j] == '1' else 0 \
        for j in range(col)] for i in range(row)]
        
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                else:
                    dp[i][j] = 0
                    
        for row in dp:
            res = max(res, max(row))
        return res*res

