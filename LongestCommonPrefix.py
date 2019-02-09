class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        
        if (not len(strs)):
            return ""
        
        if (len(strs) == 1):
            return strs[0]
    
        firstStr = strs[0]
        strs = strs[1:]
        currentPrefix = ""
        for i in range(len(firstStr)):
            for j in strs:

                if not j.startswith(firstStr[:i + 1]):
                    return currentPrefix

            
            currentPrefix = firstStr[:i + 1]

        return currentPrefix

class Solution2:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        pass

if __name__ == "__main__":
    Solution().longestCommonPrefix(["c","c"])