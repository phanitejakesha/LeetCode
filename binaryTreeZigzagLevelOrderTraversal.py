#inary Tree Zigzag Level Order Traversal
#leetcode 103


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        q = []
        q.append(root)
        res =[]
        count = 0
        while len(q)!=0:
            newQ = []
            ans =[]
            while len(q)!=0:
                r = q.pop(0)
                ans.append(r.val)
                if r.left!=None:
                    newQ.append(r.left)
                if r.right!=None:
                    newQ.append(r.right)
            if count%2==0:
                res.append(ans)
            else:
                res.append(ans[::-1])
            count+=1
            q = newQ
        return res
            
