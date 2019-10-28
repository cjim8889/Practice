class Solution:
    def combinationSum(self, candidates, target):
        
        result = []
        dic = dict()
        self.find(sorted(candidates), target, 0, result, [], dic)

        return result

    def find(self, candidates, target, index, result, current, dic):
        if (f"{target}" in dic):
            result.append(current + dic[f"{target}"])
            return (False, [])

        if (target < 0):
            return (False, [])

        if (target == 0):
            result.append(current)
            return (True, current)

        for i in range(index, len(candidates)):
            ret, path = self.find(candidates, target - candidates[i], i, result, current + [candidates[i]], dic)
            if (ret):
                dic[f"{target - candidates[i]}"] = path[len(current) + 1:]


        return (False, [])
        
        
if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum([2, 3, 6, 7], 7))


