#Leetcode problem Number 35
#Find ancestor of the nodes 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return 
        if p.val<root.val and q.val>root.val or p.val>root.val and q.val<root.val:
            return root
        self.ans=[]
        self.path(root,'',p,q)
        path1 = self.ans[0]
        path2 = self.ans[1]
        l1 = path1.split('->')
        l2 = path2.split('->')
        #print(l1,l2)
        if len(l1)<len(l2):
            x = len(l1)
        else:
            x = len(l2)
        for i in range(0,x):
            if l1[i]!=l2[i]:
                #print(l1[i-1])
                self.ansNode = None
                self.findNode(root,int(l1[i-1]))
                return self.ansNode
        self.ansNode = None
        self.findNode(root,int(l1[x-1]))
        return self.ansNode
            
            
        
    def path(self,root,givenPath,p,q):
        if root is None:
            return 
        if root.val==p.val:
            self.ans.append(givenPath+str(root.val))           
        if root.val==q.val:
            self.ans.append(givenPath+str(root.val))
        self.path(root.left,givenPath+str(root.val)+'->',p,q)
        self.path(root.right,givenPath+str(root.val)+'->',p,q)
        
    def findNode(self,root,val):
        if root is None:
            return 
        #print(root.val,val)
        if root.val==val:
            #print(root.val)
            self.ansNode = root
        self.findNode(root.left,val)
        self.findNode(root.right,val)
        
