class Solution:
    def strStr(self, haystack: 'str', needle: 'str') -> 'int':

        if (not len(needle)):
            return 0

        if (not len(haystack) or len(needle) > len(haystack)):
            return -1 
        
        for i, v in enumerate(haystack):


            if (v == needle[0]):
                if (haystack[i + 1:i + len(needle)] == needle[1:]):
                    return i              


        return -1  


class Solution2:
    def strStr(self, haystack: 'str', needle: 'str') -> 'int':

        if (not len(needle)):
            return 0


        l = len(needle)
        i = 0
        while (len(haystack) - i >= l):
            
            if (haystack[i:i + l] == needle):
                return i
            
            i += 1

        return -1

if __name__ == "__main__":
    print(Solution2().strStr("Hello", "Hello"))