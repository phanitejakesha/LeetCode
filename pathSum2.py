#Leetcode problem Number 113
#Path sum 2  
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.ans=[]
        self.path(root,'')
        result = []
        for i in range(0,len(self.ans)):
            li = self.ans[i].split('->')
            parRes = 0
            for key in li:
                parRes+=int(key)
            if parRes == sum:
                for j in range(0,len(li)):
                    li[j]=int(li[j])
                result.append(li)
        return result
                
        
        
        
    def path(self,root,givenPath):
        if root is None:
            return 
        if root.left is None and root.right is None:
            self.ans.append(givenPath+str(root.val))
        self.path(root.left,givenPath+str(root.val)+'->')
        self.path(root.right,givenPath+str(root.val)+'->')
        
