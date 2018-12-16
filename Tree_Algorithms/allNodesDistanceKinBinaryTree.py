#Leetcode problem Number 863
#All nodes distance K in binary tree
"""
Author: Phani Teja Kesha

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class graphNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.par = None
    
class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        if root is None:
            return []
        self.addParent(root,par = None)
        #find the node of the value 
        self.kNode = None
        self.inOrder(root,target.val)
        q = []
        q.append(self.kNode)
        seen =set()
        count = 0
        ans =[]
        while len(q)!=0:
            newQ = []
            while len(q)!=0:
                x  = q.pop(0)
                if x in seen:
                    continue
                seen.add(x)
                if count == K:
                    ans.append(x.val)
                if x.left!=None:
                    newQ.append(x.left)
                if x.right!=None:
                    newQ.append(x.right)
                if x.par!=None:
                    newQ.append(x.par)
            count+=1
            q = newQ        
        return ans
    
    def addParent(self,root1,par):
        if root1:
            root1.par = par
            self.addParent(root1.left,root1)
            self.addParent(root1.right,root1)
    
    
    def inOrder(self,root,v):
        if root is None:
            return 
        self.inOrder(root.left,v)
        if root.val==v:
            self.kNode = root
        self.inOrder(root.right,v)
