class Tree(object):
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r

class Solution:
    def findTilt(self, root):
        self.tilt = 0
        self.postOrder(root)
        return self.tilt

    def postOrder(self,root):
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        l = self.postOrder(root.left)
        r = self.postOrder(root.right)
        self.tilt += abs(l-r)
        return l+r + root.val

b = Tree(2, None,None)
a = Tree(10, None,None)
c = Tree(6, None,None)
d = Tree(12, None,None)

left = Tree(2, b, a)
right= Tree(3, c, d)
# right=Tree(20,a,b)
root = Tree(1, left,right)

sol = Solution()
print(sol.findTilt(root))