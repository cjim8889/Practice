class Solution:
    def minCostClimbingStairs(self, cost: 'List[int]') -> 'int':
        self.minCosts = dict()
        self.length = len(cost)

        cost0 = self._minCost(0, cost)
        cost1 = self._minCost(1, cost)

        return cost0 if cost0 < cost1 else cost1

    def _minCost(self, i, cost):
        
        if (not i < self.length):
            return 0

        if (i in self.minCosts):
            return self.minCosts[i]
        

        a = self._minCost(i + 1, cost)
        b = self._minCost(i + 2, cost)

        self.minCosts[i] = cost[i] + a if a < b else cost[i] + b

        return self.minCosts[i]

if __name__ == "__main__":
    print(Solution().minCostClimbingStairs([10,15,20]))