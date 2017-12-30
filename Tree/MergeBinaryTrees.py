class Tree(object):
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r

class Solution:
    def mergeTrees(self, t1, t2):
        self.merge(t1,t2)
        return t1

    def merge(self,t1,t2):
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val+=t2.val
        t1.left = self.merge(t1.left,t2.left)
        t1.right = self.merge(t1.right,t2.right)


b = Tree(5, None,None)
left = Tree(3, b, None)
right=Tree(2,None, None)
root = Tree(1, left,right)

b1 = Tree(7, None,None)
a = Tree(4, None,None)
left1 = Tree(1, None, a)
right1=Tree(3,None,b1)
root1 = Tree(2, left1,right1)

sol = Solution()
