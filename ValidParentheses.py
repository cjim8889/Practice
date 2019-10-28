class Solution:
    def isValid(self, s: 'str') -> 'bool':
        if (len(s) % 2 != 0):
            return False


        dic = {"}": "{", ")" : "(", "]" : "["}
        stack = []


        for j in s:
            if(not stack):
                stack.append(j)
                continue

            val = stack.pop()
            if (j not in dic):
                stack.append(val)
                stack.append(j)
            elif (val == dic[j]):
                continue
            else:
                return False

        return len(stack) == 0

if __name__ == "__main__":
    
    print(Solution().isValid("[[{}]]"))