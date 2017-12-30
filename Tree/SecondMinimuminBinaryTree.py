class Tree(object):
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r

class Solution(object):
    def findSecondMinimumValue(self, root):
        self.secondmin = float('inf')
        self.findateach(root)
        if root.val == self.secondmin or self.secondmin == float('inf'):
            return -1
        return self.secondmin

    def findateach(self,root):
        if not root:
            return None
        if root.left and root.right:
            if root.left.val<root.right.val:
                self.secondmin = min(root.right.val, self.secondmin)
                self.findateach(root.left)
            elif root.left.val>root.right.val:
                self.secondmin = min(root.left.val, self.secondmin)
                self.findateach(root.right)
            else:
                self.findateach(root.right)
                self.findateach(root.left)



b = Tree(2, None,None)
a = Tree(2, None,None)
c = Tree(1, None,None)
d = Tree(1, None,None)
# left = Tree(1, c, d)
left = Tree(1,None, None)
# right=Tree(2,a,b)
right=Tree(2,None,None)
root = Tree(2, left,right)

sol = Solution()
print(sol.findSecondMinimumValue(root))