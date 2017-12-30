class Tree(object):
    def __init__(self, x, l = None, r = None):
        self.val = x
        self.left = l
        self.right = r

class Solution(object):
    def binaryTreePaths(self, root):
        self.path = []
        self.findpaths(root, '')
        return self.path

    def findpaths(self, root, curr):
        if not root:
            return None
        if not root.left and not root.right:
            curr = curr + str(root.val)
            self.path.append(curr)
        else:
            curr = curr + str(root.val) + '->'
            self.findpaths(root.left, curr)
            self.findpaths(root.right, curr)

b = Tree(5, None,None)
left = Tree(2, None, b)
right= Tree(3, None, None)
root = Tree(1, left,right)

sol = Solution()
print(sol.binaryTreePaths(root))
