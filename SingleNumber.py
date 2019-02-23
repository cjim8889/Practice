class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'int':
        # xor logical way of doing this question

        n = 0
        for i in nums:
            n ^= i
        
        return n

class Solution2:
    def singleNumber(self, nums: 'List[int]') -> 'int':
        
        table = dict()

        for i in nums:
            
            if (i not in table):
                table[i] = 1
            else:
                table.pop(i)

        
        return table.popitem()[0]