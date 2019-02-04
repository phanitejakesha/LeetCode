#Leetcode problem Number 988
#smallest string starting from leaf
# Definition for a binary tree node

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ''
        self.ans=[]
        self.path(root,'')
        result = []
        for i in range(0,len(self.ans)):
            li = self.ans[i].split('->')
            result.append(li)
        ans = []
        for i in range(0,len(result)):
            preRes = []
            for j in range(0,len(result[i])):
                c = chr(int(result[i][j])+97)
                preRes.append(c)
            ans.append(''.join(preRes)[::-1])
        ans.sort()
        return ans[0]
                        
    def path(self,root,givenPath):
        if root is None:
            return 
        if root.left is None and root.right is None:
            self.ans.append(givenPath+str(root.val))
        self.path(root.left,givenPath+str(root.val)+'->')
        self.path(root.right,givenPath+str(root.val)+'->')
        
