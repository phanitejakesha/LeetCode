#Leetcode 145
#Binary tree postorder traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans =[]
        self.ITrans(root,ans)
        return ans
    
    
    def ITrans(self, root,ans):
        if root is None:
            return [] 
        self.ITrans(root.left,ans)
        self.ITrans(root.right,ans)
        ans.append(root.val)
        

