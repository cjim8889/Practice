class Solution:
    def climbStairs(self, n: 'int') -> 'int':
        
        self.count = 0
        self.dictionary = dict()
        self.count = self._climbStairs(n, 0)
        return self.count

    def _climbStairs(self, n, c):

        if (c > n):
            return 0
        
        if (c == n):
            return 1
        
        if (c in self.dictionary):
            return self.dictionary[c]

        i = self._climbStairs(n, c + 1) + self._climbStairs(n, c + 2)
        self.dictionary[c] = i
        return i 



if __name__ == "__main__":
    Solution().climbStairs(34)
