'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''
'''
class Solution(object):
    def minPathSum(self, grid):
        
        #此数组用于记忆化搜索
        dp = [[0]*len(grid[0]) for i in range(len(grid))]

        for i in range(len(grid)):

            for j in range(len(grid[0])):

                #在起点的时候
                if (i == 0 and j == 0):
                    dp[i][j] = grid[0][0]

                #在左边缘的时候
                elif (j == 0 and i != 0):
                    dp[i][j] = dp[i - 1][j]  + grid[i][j]

                #在上边缘的时候
                elif (i == 0 and j != 0):
                    dp[i][j] = dp[i][j-1] + grid[i][j]

                # 普遍情况下
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
                    
        return dp[len(grid)-1][len(grid[0])-1]
'''
'''class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 显然是动态规划
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i==0 and j==0:
                    continue
                elif i==0:
                    grid[i][j] = grid[i][j-1] + grid[i][j]
                elif j==0:
                    grid[i][j] = grid[i-1][j] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        
        return grid[-1][-1]
'''
class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0: continue
                #都等于0 时起始点
                elif i == 0:  grid[i][j] = grid[i][j - 1] + grid[i][j]
                #左边是墙
                elif j == 0:  grid[i][j] = grid[i - 1][j] + grid[i][j]
                #上边是墙
                else: grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
                #在中间的点
        return grid[-1][-1]
