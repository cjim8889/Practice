class Solution:
    # Naive
    def maxArea(self, height: 'List[int]') -> int:
        i = 0
        j = len(height) - 1
        width = len(height) - 1

        maxVolume = width * min(height[i], height[j])

        
        while (i < j):
            
            k = (width - 1) * min(height[i], height[j - 1])
            
            if (k > maxVolume):
                j -= 1
                width -= 1
                maxVolume = k
            
            l = (width - 1) * min(height[i + 1], height[j])

            if (l > maxVolume):
                i += 1
                width -= 1
                maxVolume = l
                continue
            
            break


        return maxVolume

class Solution2:
    def maxArea(self, height: 'List[int]') -> int:
        i = 0
        j = len(height) - 1
        width = len(height) - 1

        maxVolume = width * height[i] if height[i] < height[j] else width * height[j]
        while(i < j):
            
            if (height[j] > height[i]):
                
                i += 1
                width -= 1

                t = width * height[i] if height[i] < height[j] else width * height[j]
                maxVolume = maxVolume if maxVolume > t else t

            else:

                j -= 1
                width -= 1

                t = width * height[i] if height[i] < height[j] else width * height[j]
                maxVolume = maxVolume if maxVolume > t else t
                    
        return maxVolume







if __name__ == "__main__":
    print(Solution2().maxArea([2,3,4,5,18,17,6]))