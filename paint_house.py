class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        def calcCellMin(row, col):
            if col is 0:
                costs[row][col] += min(costs[row + 1][1], costs[row + 1][2])
            if col is 1:
                costs[row][col] += min(costs[row + 1][0], costs[row + 1][2])
            if col is 2:
                costs[row][col] += min(costs[row + 1][1], costs[row + 1][0])
            return costs[row][col]
        
        for row in range(len(costs) - 2, -1, -1):
            for col in range(3):
                calcCellMin(row, col)
        
        return min(costs[0])
