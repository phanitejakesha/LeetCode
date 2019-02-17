#Leetcode problem Number 93
#cousions in binary tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if root is None:
            return 
        self.ans=[]
        self.path(root,'',x,y)
        path1 = self.ans[0]
        path2 = self.ans[1]
        l1 = path1.split('->')
        l2 = path2.split('->')
        print(l1,l2)
        if len(l1)!=len(l2):
            return False
        if l1[len(l1)-2]==l2[len(l2)-2]:
            return False
        return True        
            
            
        
    def path(self,root,givenPath,p,q):
        if root is None:
            return 
        if root.val==p:
            self.ans.append(givenPath+str(root.val))           
        if root.val==q:
            self.ans.append(givenPath+str(root.val))
        self.path(root.left,givenPath+str(root.val)+'->',p,q)
        self.path(root.right,givenPath+str(root.val)+'->',p,q)
        
 
        


        
