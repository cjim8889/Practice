def twoSum(nums: 'List[int]', target: 'int') -> 'List[int]':
    
    dictionary = { value:index for (index, value) in enumerate(nums)}


    for (i,v) in enumerate(nums):

        targetNum = target - v

        if targetNum in dictionary and dictionary[targetNum] != i:
            
            return [i, dictionary[targetNum]]







if __name__ == "__main__":
    print(twoSum([3,2,4], 6))