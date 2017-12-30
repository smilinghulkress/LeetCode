class Tree(object):
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r

class Solution(object):
    def findMode(self, root):
        self.m = 0
        self.count = 0
        self.reverseInorder(root,root.val)
        print(max(self.m,self.count))


    def reverseInorder(self, root,k):
        if not root:
            return None
        if root.val == k:
            self.count+=1
        else:
            print(root.val, self.count)
            self.m = max(self.m, self.count)
            self.count=1
            k = root.val
        self.reverseInorder(root.right,k)
        self.reverseInorder(root.left,k)

b = Tree(17, None,None)
a = Tree(2, None,None)
left = Tree(2, None, None)
# right= Tree(20, a, b)
right=Tree(2,a,None)
root = Tree(1, left,right)

sol = Solution()
sol.findMode(root)