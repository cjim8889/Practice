class Solution:
    def removeElement(self, nums: 'List[int]', val: 'int') -> 'int':

        if (not len(nums)):
            return 0


        j = 0
        l = len(nums)

        while (j < l):

            if (nums[j] == val):

                nums[j] = nums[l - 1]
                l -= 1
            else:

                j += 1

        return j



if __name__ == "__main__":
    Solution().removeElement([0,1,2,2,3,0,4,2], 2)


