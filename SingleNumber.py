class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'int':
        # xor logical way of doing this question

        n = 0
        for i in nums:
            n ^= i
        
        return n