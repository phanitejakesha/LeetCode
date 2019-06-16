class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr):
            if arr[i]==0:
                if i+1 < len(arr):
                    j = i+1
                    temp = arr[j]
                    arr[j] = 0
                    while j < len(arr)-1:
                        temp2 = temp
                        temp = arr[j+1]
                        arr[j+1] = temp2
                        j+=1
                    i+=1 
                i+=1
            else:
                i+=1
