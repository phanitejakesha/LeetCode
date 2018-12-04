#Leetcode problem Number 530
#Minimum Absolute differennce in BST

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = []
        self.callInorder(root)
        ans = sorted(self.ans)
        result = []
        for i in range(0,len(ans)-1):
            result.append(ans[i+1]-ans[i])
        return min(result)
    def callInorder(self,root):
        if root is None:
            return 
        self.callInorder(root.left)
        self.ans.append(root.val)
        self.callInorder(root.right)
        
