class Solution:
    # Kadane's algorithm
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        # s = sum(nums)
        if (len(nums) == 1):
            return nums[0]
        
        sum = nums[0]
        csum = sum


        for i in nums[1:]:

            csum = i if i >= csum + i else csum + i
            sum = sum if sum >= csum else csum
            
        return sum

class Solution2:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        # s = sum(nums)
        if (len(nums) == 1):
            return nums[0]
        
        i = 0
        j = len(nums) - 1

        iFlag = False
        jFlag = False

        while (not iFlag and not jFlag):

            if (not i + 1 < len(nums)):
                break
            
            if (not j - 1 > -1):
                break


            if (nums[i] + nums[i + 1] < 0):
                i += 1
            elif (nums[i] < 0 and nums[i + 1] >= 0):
                i += 1
            else:
                iFlag = True

            if (i >= j - 1):
                break

            if (nums[j] + nums[j - 1] < 0):
                j -= 1
            elif (nums[j] < 0):
                j -= 1
            else:
                jFlag = True
            



        # print(i, j)
        # print(sum(nums[i: j + 1]))
        return sum(nums[i: j + 1])


if __name__ == "__main__":
    
    A = [-2,1,-3,4,-1,2,1,-5,4]

    Solution().maxSubArray(A)
