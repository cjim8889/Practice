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
        
        if (not len(strs)):
            return ""
        elif (len(strs) == 1):
            return strs[0]

        firstStr = strs[0]
        prefix = ""
        lengthList = [len(i) for i in strs]
        strs = strs[1:]
        

        for i in range(min(lengthList)):

            for j in strs:
                
                if (not j[i] == firstStr[i]):
                    return prefix

            prefix = firstStr[:i + 1]
        return prefix
            






if __name__ == "__main__":
    Solution2().longestCommonPrefix(["","b"])