from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        orderedList = sorted(nums)
        print(orderedList)

        result = []
        temp = []

        self.backtrack(result, nums, temp, target, 0)
        return result
        
    def backtrack(self, result, nums, temp, remain, index):
        if (len(temp) > 4):
            return

        if (remain == 0 and len(temp) == 4):
            if (temp in result):
                return
            result.append(temp.copy())
            return

        for i in range(index, len(nums)):
            temp.append(nums[i])
            self.backtrack(result, nums, temp, remain - nums[i], i + 1)
            temp.pop()

class Solution2:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        orderedList = sorted(nums)
        dic = dict()
        for i in range(len(orderedList)):
            for j in range(i + 1, len(orderedList)):
                dic[orderedList[i] + orderedList[j]] = [orderedList[i], orderedList[j]]

        
        result = self.twoSum(sorted(list(dic.keys())), target)

        res = []
        for r in result:
            res.append(dic[r[0]] + dic[r[1]])


        return res

    def twoSum(self, nums, target):
        l = 0
        r = len(nums) - 1

        result = []
        while (l != r and l < r):
            s = nums[l] + nums[r]
            if (s < target):
                l += 1
            elif (s == target):
                result.append([nums[l], nums[r]])
                l += 1
                r -= 1
            else:
                r -= 1
    
        return result
                
if __name__ == "__main__":
    s = Solution2()
    s.fourSum([1, 0, -1, 0, -2, 2], 0)