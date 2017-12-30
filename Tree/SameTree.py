# Definition for a binary tree node.
class Tree(object):
    def __init__(self, x, l = None, r = None):
        self.val = x
        self.left = l
        self.right = r

class Solution(object):
    def isSameTree(self, p, q):
        return self.checkOrder(p,q)

    def checkOrder(self, p, q):
        if not p and not q:
            return True
        elif not p and q:
            return False
        elif not q and p:
            return False

        if p.val != q.val:
            return False
        elif p.val == q.val:
            k = self.checkOrder(p.left, q.left)
            l = self.checkOrder(p.right, q.right)
            return k and l


# a = Tree(2,None,None)
# b = Tree(4, None,None)
# c = Tree(7,None,None)
# # left = Tree(3, a, b)
# # left = Tree(3, None, None)
# # right = Tree(6, None, c )
right= Tree(2, None, None)
root = Tree(1, None,right)

# d = Tree(2,None,None)
# e = Tree(4, None,None)
# f = Tree(7,None,None)
# l = Tree(3, d, e)
l = Tree(2, None, None)
# r = Tree(6, None, f )
# r= Tree(13, None, None)
k = Tree(1, l,None)

sol = Solution()
print(sol.isSameTree(k,root))
