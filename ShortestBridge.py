from collections import deque
class Solution:
    def shortestBridge(self, A):
        # self.printList(A)
        queue, distanceList = self.dfs(A)
        res = self.bfs(A, queue, distanceList)
        return res

    def bfs(self, list, queue, distanceList):

        min_length = 99999999
        result = []

        while len(queue) > 0:
            y, x = queue.popleft()

            list[y][x] = -1

            if (y + 1 < len(list)):
                if (list[y + 1][x] == 1):
                    result.append(distanceList[y][x] + 1)
                elif (list[y + 1][x] == 0):
                    queue.append([y + 1, x])
                    
                    if (distanceList[y + 1][x] == -1):
                        distanceList[y + 1][x] = distanceList[y][x] + 1
            
            if (x + 1 < len(list[y])):
                if (list[y][x + 1] == 1):
                    result.append(distanceList[y][x] + 1)
                elif (list[y][x + 1] == 0):
                    queue.append([y, x + 1])
                    if (distanceList[y][x + 1] == -1 ):
                        distanceList[y][x + 1] = distanceList[y][x] + 1

            if (y - 1 > -1):
                if (list[y - 1][x] == 1):
                    result.append(distanceList[y][x] + 1)
                elif (list[y - 1][x] == 0):
                    queue.append([y - 1, x])
                    if (distanceList[y - 1][x] == -1):
                        distanceList[y - 1][x] = distanceList[y][x] + 1
            
            if (x - 1 > -1):
                if (list[y][x - 1] == 1):
                    result.append(distanceList[y][x] + 1)
                elif (list[y][x - 1] == 0):
                    queue.append([y, x - 1])
                    if (distanceList[y][x - 1] == -1 ):
                        distanceList[y][x - 1] = distanceList[y][x] + 1

        return min(result) - 1

    def dfs(self, li):

        stack = deque()
        queue = deque()
        

        f = False
        for i in range(len(li)):
            for j in range(len(li[i])):
                if (li[i][j] == 1):
                    stack.append([i, j])
                    f = True
                    break
            
            if (f):
                break
                

        distanceList = [[-1]*len(li[i]) for i in range(len(li))]

        while len(stack) > 0:

            y, x = stack.pop()
            queue.append([y, x])
            li[y][x] = -1
            distanceList[y][x] = 0

            if (y + 1 < len(li)):
                if (li[y + 1][x] == 1):
                    stack.append([y + 1, x])
            
            if (x + 1 < len(li[y])):
                if (li[y][x + 1] == 1):
                    stack.append([y, x + 1])

            if (y - 1 > -1):
                if (li[y - 1][x] == 1):
                    stack.append([y - 1, x])
            
            if (x - 1 > -1):
                if (li[y][x - 1] == 1):
                    stack.append([y, x - 1])




        return (queue, distanceList)