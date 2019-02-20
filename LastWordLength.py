class Solution:
    def lengthOfLastWord(self, s: 'str') -> 'int':
        if (len(s) == 0):
            return 0


        length = 0
        lengthS = len(s)

        flag = False
        for i in range(lengthS):
            if (s[lengthS - 1 - i] != ' '):
                flag = True
                length += 1
            else:
                if (flag):
                    break
        return length


if __name__ == "__main__":
    Solution().lengthOfLastWord("Hello World")