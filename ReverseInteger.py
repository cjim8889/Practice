class Solution:
    def reverse(self, x: 'int') -> 'int':

        negative = x < 0
        x = abs(x)
        result = 0

        while (x):
            
            remainder = x % 10
            result = result * 10 + remainder
            x = x // 10
        
        if negative:
            result *= -1
        
        if not -2147483648 <= result <= 2147483647:
            result = 0

            
        return result

if __name__ == "__main__":
    
    Solution().reverse(-123)