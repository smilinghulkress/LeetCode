class Tree(object):
    def __init__(self, x, l = None, r = None):
        self.val = x
        self.left = l
        self.right = r
class Solution(object):
    def sumOfLeftLeaves(self, root):
        self.sum =0
        self.traverse(root,False)
        return self.sum

    def traverse(self,root,leftFlag):
        if not root:
            return None
        if leftFlag == True and not root.left and not root.right:
            self.sum+= root.val

        self.traverse(root.left,True)
        self.traverse(root.right,False)

b = Tree(17, None,None)
a = Tree(15, None,None)
left = Tree(9, None, None)
# right= Tree(20, a, b)
right=Tree(20,None,None)
root = Tree(3, left,right)

sol = Solution()
print(sol.sumOfLeftLeaves(root))