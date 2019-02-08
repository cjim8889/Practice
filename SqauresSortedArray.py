class Solution:
    def sortedSquares(self, A: 'List[int]') -> 'List[int]':
        
        index = -1
        for i in range(len(A)):
            
            if (A[i] >= 0):
                index = i
                break
        
        for i in range(index):

            A[i] = - A[i]

        A.sort()

        return [i*i for i in A]
if __name__ == "__main__":
    Solution().sortedSquares(l)