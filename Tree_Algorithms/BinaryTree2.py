# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root:
            flag = True
        else:
            return TreeNode(val)
        node = root
        prev = None
        while(node):
            if val < node.val:
                prev = node
                node = node.right
            else:
                newNode = TreeNode(val)
                newNode.left = node
                if prev is not None:
                    prev.right = newNode
                else:
                    root = newNode
                break
        if node is None:
            prev.right = TreeNode(val)
        
        return root
        
