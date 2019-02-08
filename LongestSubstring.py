class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        
        output = 0
        start = 0
        dic = {}
        for index, val in enumerate(s):
            if val in dic and dic[val] >= start:

                start = dic[val] + 1
                dic[val] = index

            else:
                # print(s[start:index + 1])
                output = max(output, index - start + 1)
                dic[val] = index
                
        
        return output




if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("bbbbb"))


