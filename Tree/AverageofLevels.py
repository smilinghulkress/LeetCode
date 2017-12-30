from collections import deque
class Tree(object):
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r

class Solution(object):
    def averageOfLevels(self, root):
        avg = []
        q= deque()
        q.append(root)
        while(q):
            k = len(q)
            levelavg = 0
            for i in range(0,k):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                levelavg+= node.val
            avg.append(levelavg/k)
        return avg


b = Tree(7, None,None)
a = Tree(15, None,None)
left = Tree(9, None, None)
# right= Tree(20, a, b)
right=Tree(20,a,b)
root = Tree(3, left,right)

sol = Solution()
print(sol.averageOfLevels(root))