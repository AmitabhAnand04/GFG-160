class Solution:
    def pushZerosToEnd(self, arr, n = None):
        if n is None:
            n = len(arr)
        
        pos = 0

        for i in range(n):
            if arr[i] != 0:
                arr[i], arr[pos] = arr[pos], arr[i]
                pos += 1

arr = [1, 2, 0, 4, 3, 0, 5, 0]
Solution().pushZerosToEnd(arr=arr)
print(arr)