class Solution:
    def toLowerCase(self, str: 'str') -> 'str':
        
        dict = {k:v for (k, v) in zip(range(ord("A"), ord("Z") + 1), range(ord("a"), ord("z") + 1))}

        rt = ""

        for c in str:
            o = ord(c)
            if (o in dict):
                rt += chr(dict[o])
            else:
                rt += c

        return rt


if __name__ == "__main__":
    sol = Solution().toLowerCase("Asd")
    print(sol)