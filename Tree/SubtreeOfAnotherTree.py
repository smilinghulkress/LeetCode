class Tree(object):
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r

class Solution:
    def isSubtree(self, s, t):
        return self.preorder(s,t)

    def preorder(self,sroot,troot):
        if not sroot:
            return False
        if sroot.val == troot.val:
            t = self.isSame(sroot, troot)
            if not t:
                return self.preorder(sroot.left, troot) or self.preorder(sroot.right, troot)
            else:
                return True
        return self.preorder(sroot.left, troot) or self.preorder(sroot.right, troot)

    def isSame(self,s,t):
        if (not s and t) or (s and not t):
            return False
        if not s and not t:
            return True
        return s.val == t.val and self.isSame(s.left,t.left) and self.isSame(s.right,t.right)


b = Tree(1, None,None)
c = Tree(2, None,None)
a = Tree(2, None,None)
d = Tree(12, None,None)
left = Tree(4, b, a)
right= Tree(5, None, None)
root = Tree(3, left,right)

left1 = Tree(1, None, None)
right1 = Tree(2, None, None)
root1 = Tree(4, left1,right1)

sol = Solution()
print(sol.isSubtree(root,root1))