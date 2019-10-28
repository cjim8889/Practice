class Solution:
    # Dynaminc programming approach
    def longestPalindrome(self, s: 'str') -> 'str':
        
        if (len(s) <= 1):
            return s
        
        self.table = [[None for j in range(0, len(s))] for i in range(0, len(s))] 

        for i in range(len(s) - 1, -1, -1):
            
            for j in range(len(s)):

                if (j + i >= len(s)):
                    break
                else:

                    if (self.isPalindrome(j, j + i, s)):
                        return s[j : j + i + 1]
                    
                
        
    def isPalindrome(self, start, end, string):
        
        if (self.table[start][end] is not None):
            return self.table[start][end]

        if (start == end):
            self.table[start][end] = True
            return True

        if (string[start] != string[end]):
            self.table[start][end] = False
            return False

        else:

            if (start + 1 <= end - 1):
                self.table[start][end] = self.isPalindrome(start + 1, end - 1, string)
            else:
                self.table[start][end] = True
            
            return self.table[start][end]




    def printTable(self, table):

        for i in table:
            print(i)
class Solution2:
    # Folding Approach
    def longestPalindrome(self, s: 'str') -> 'str':
        
        result = ""

        for i in range(len(s)):
            
            for j in range(i + 1, len(s)):
                pass


if __name__ == "__main__":
    #  a|b|a
    print(Solution().longestPalindrome("abbbbbbbbba"))