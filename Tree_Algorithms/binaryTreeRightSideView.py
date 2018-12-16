#Leetcode problem Number 199
#Binary Tree Right side view

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        ans = []
        thislevel = [root]
        while thislevel:
            nextlevel = []
            x = []
            for n in thislevel:
                x.append(n.val)
                if n.left: 
                    nextlevel.append(n.left)
                if n.right: 
                    nextlevel.append(n.right)
            ans.append(x)
            thislevel = nextlevel
        result = []
        for i in range(0,len(ans)):
            result.append(ans[i][len(ans[i])-1])
        return result
