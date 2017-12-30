# Definition for a binary tree node.
class Tree(object):
    def __init__(self, x, l = None, r = None):
        self.val = x
        self.left = l
        self.right = r

class Solution(object):
    complement = {}
    def findTarget(self, root, k):
        return self.preOrder(root,k)

    def preOrder(self,root,k):
        if not root:
            return False
        if k-root.val in self.complement:
            return True
        else:
            self.complement[root.val]= True
        return self.preOrder(root.left,k) or self.preOrder(root.right,k)
        # return False

a = Tree(2,None,None)
b = Tree(4, None,None)
c = Tree(7,None,None)
left = Tree(3, a, b)
right = Tree(6, None, c )
# right= Tree(13, None, None)
root = Tree(5, left,right)

sol = Solution()
print(sol.findTarget(root, 9))