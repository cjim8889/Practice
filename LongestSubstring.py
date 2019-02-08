class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        
        
        output = 0

        while (s):
            dic = {}
            flag = False

            for i in range(len(s)):
                
                if (s[i] in dic):
                    output = max(output, i)
                    s = s[dic[s[i]] + 1:]
                    flag = True
                    break
                else:
                    dic[s[i]] = i

            if (not flag):
                return max(output, len(s))

            if (output >= len(s)):
                return output

        return output

if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))


