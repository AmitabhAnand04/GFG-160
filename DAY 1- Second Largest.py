class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        if len(arr) < 2:
            return -1
            
        first = second = float('-inf')
        
        for num in arr:
            if num > first:
                second = first
                first = num
            elif first > num > second:
                second = num
                
        return second if second != float('-inf') else -1
    
arr = [1, 2, 0, 4, 3, 0, 5, 0]
second_largest = Solution().getSecondLargest(arr=arr)
print(second_largest)