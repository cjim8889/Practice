class Solution:
    def romanToInt(self, s: 'str') -> 'int':
        dic = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000, "IV" : 4, "IX": 9, "XL" : 40, "XC" : 90, "CD" : 400, "CM" : 900}

        result = 0
        length = len(s)
        skip = False
        for i in range(length):

            if (skip):
                skip = False
                continue

            if (s[i] == "I" or s[i] == "X" or s[i] == "C"):
                
                if (i + 1 < length):

                    if (s[i:i+2] in dic):

                        result += dic[s[i:i+2]]
                        skip = True
                        continue
            
            result += dic[s[i]]
        return result

class Solution2:
    def romanToInt(self, s: 'str') -> 'int':
        dic = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}

        result = 0
        for i in range(len(s)):
            
            if (i == len(s) - 1):
                return result + dic[s[i]]
                
            if (dic[s[i]] < dic[s[i + 1]]):
                result -= dic[s[i]]
                continue
            
            result += dic[s[i]]
                

        
if __name__ == "__main__":
    Solution().romanToInt("LVIII")

