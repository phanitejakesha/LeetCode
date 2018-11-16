#Leetcode problem Number 230
#Kth smallest element in BST 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        ans =[]
        self.ITrans(root,ans)
        print(ans)
        if len(ans)<k:
            return 
        return ans[k-1]
    
    
    def ITrans(self, root,ans):
        if root is None:
            return [] 
        self.ITrans(root.left,ans)
        ans.append(root.val)
        self.ITrans(root.right,ans)
