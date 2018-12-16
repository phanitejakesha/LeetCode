#Leetcode problem Number 429
#N-ary Tree Level Order traversal

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        q = []
        q.append(root)
        res =[]
        while len(q)!=0:
            qNew =[]
            ans = []
            while len(q)!=0:                
                r = q.pop(0)
                ans.append(r.val)
                #print(r.val)
                for i in range(0,len(r.children)):
                    qNew.append(r.children[i])
            q = qNew
            res.append(ans)
        return res
            
            
