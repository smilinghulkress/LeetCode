class Tree(object):
    def __init__(self, x, l = None, r = None):
        self.val = x
        self.left = l
        self.right = r

class Solution(object):
    sum = 0
    def convertBST(self, root):
        self.reverseInorder(root)
        return root

    def reverseInorder(self, root):
        if not root:
            return None
        self.reverseInorder(root.right)
        # k= root.val
        self.sum+=root.val
        root.val = self.sum
        self.reverseInorder(root.left)


a = Tree(9,None,None)
b = Tree(15, None,None)
left = Tree(2, None, None)
# right = Tree(13, a,b )
right= Tree(13, None, None)
root = Tree(5, left,right)

# print(root.val, root.left.val, root.right.val)
sol = Solution()
k = sol.convertBST(root)
print(k.val, k.left.val, k.right.val)