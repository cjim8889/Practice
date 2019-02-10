class Solution:
    def isPalindrome(self, x: 'int') -> 'bool':
        if x == 0:
            return True

        if x % 10 == 0 or x < 0:
            return False

        original = x
        reversed = 0

        while (x):
            
            digit = x % 10
            x = x // 10

            reversed *= 10
            reversed += digit
            
        return reversed == original

if __name__ == "__main__":
    Solution().isPalindrome(0)
