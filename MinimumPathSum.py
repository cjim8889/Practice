from typing import List
class Solution:
    def minPathSum(self, grid):
        path = [[-1 for _ in range(len(grid[j]))] for j in range(len(grid))]
        costTable = [[-1 for _ in range(len(grid[j]))] for j in range(len(grid))]
        self.constructPath(grid, path, costTable)
        return 0

    def constructPath(self, grid, path, costTable):

        self.cost(grid, len(grid[0]), len(grid), path, costTable, 0, 0)
        
        for k in path:
            print(k)

        for l in grid:
            print(l)
        
        

    def cost(self, grid, m, n, path, costTable, x, y):
        # 0: down, 1: right
        if (not x < m):
            return -1
        
        if (not y < n):
            return -1


        if (costTable[y][x] != -1):
            return costTable[y][x]
        
        if (x + 1 == m and y + 1 == n):
            return grid[y][x]

        selfCost = grid[y][x]
        right = self.cost(grid, m, n, path, costTable, x + 1, y)
        down = self.cost(grid, m, n, path, costTable, x, y + 1)
        print(right, down, f"({x},{y})")
        if (right > down and right != -1):
            path[y][x] = 0
            costTable[y][x] = selfCost + right
        elif (down <= right and down != -1):
            path[y][x] = 1
            costTable[y][x] = selfCost + down

        # print(path)s
        return costTable[y][x]

if __name__ == "__main__":
    path = [
        [1,3,1],
        [1,5,1],
        [4,2,1]
    ]

    s = Solution().minPathSum(path)
    print(s)