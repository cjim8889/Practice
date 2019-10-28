class Solution:
    def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        
        s = sum([i for i in A if i % 2 == 0]) or 0
        res = []
        for v, i in queries:
            

            if (A[i] % 2 == 0):
                
                if(v % 2 == 0):
                    s += v
                else:
                    s -= A[i]

            else:

                if (not v % 2 == 0):
                    s += v + A[i]

            A[i] += v

            res.append(s)
        
        return res

                

                