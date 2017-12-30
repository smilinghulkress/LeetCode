from collections import deque
class Tree(object):
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r
class Solution:
    def levelOrderBottom(self, root):
        self.normal = []
        self.levelOrder(root)
        return self.normal
    def levelOrder(self,root):
        if not root:
            return None
        q = deque()
        q.append(root)
        while q:
            k = len(q)
            temp = []
            print('Next')
            for i in range(k):
                node = q.popleft()
                print("Node",node.val)
                if node.left:
                    print('Left', node.left.val)
                    q.append(node.left)
                if node.right:
                    print('Right', node.right.val)
                    q.append(node.right)
                temp.append(node.val)
            self.normal.insert(0,temp)
b = Tree(7, None,None)
a = Tree(15, None,None)
left = Tree(9, None, None)
# right= Tree(20, None, None)
right=Tree(20,a,b)
root = Tree(3, left,right)

sol = Solution()
print(sol.levelOrderBottom(root))