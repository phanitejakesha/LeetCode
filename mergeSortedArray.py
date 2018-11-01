#Leetcode Question Number 88
#Merge Sorted Array


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        k = m-1
        for i in range(len(nums1)-1,-1,-1):
            nums1[i] = nums1[k]
            k-=1
        i = 0
        j = 0
        k = 0 
        #print(nums1)
        #print(nums2)
        while n+i<len(nums1) and j<len(nums2):
            #print(nums1[n+i],nums2[j])
            #print(n+i,j)
            if nums1[n+i]<=nums2[j]:
                nums1[k]=nums1[n+i]
                i+=1
            else:
                nums1[k]=nums2[j]
                j+=1
            #print(nums1)
            k+=1
        while n+i<len(nums1):
            nums1[k]=nums1[n+i]
            k+=1
            i+=1
        while j<len(nums2):
            #print(k,j)
            #print(nums1)
            nums1[k]=nums2[j]
            j+=1
            k+=1
            
