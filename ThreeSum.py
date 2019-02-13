class Solution:


    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':

        if (len(nums) < 3):
            return []

        dic = {}
        for k, i in enumerate(nums):
            

            if not i in dic:
                dic[i] = [k]
            else:
                dic[i].append(k)
        
        result = []
        resultSet = set()

        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i == j):
                    continue

                target = -(nums[i] + nums[j])
                index = None
                if (target in dic):
                    for k in dic[target]:
                        if (k != i and k != j):
                            index = k
                            break
                else:
                    continue

                if (index is None):
                    continue

                l = [nums[i], nums[j], nums[index]]
                l.sort()
                resultSet.add(str(l))

        for i in resultSet:
            b = i[1:-1].split(",")
            b = list(map(lambda i: int(i), b))
            result.append(b)


        return result


if __name__ == "__main__":
    Solution().threeSum([-1,0,1,2,-1,-4])



