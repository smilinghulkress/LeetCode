from collections import deque


class Tree(object):
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r


class Solution:
    def zigzagLevelOrder(self, root):
        ret = []
        tree = []  # Stack
        q = []
        if not root:
            return ret
        q.append(root)
        while q or tree:
            temp =[]
            while q:
                node = q.pop()
                temp.append(node.val)
                if node.left:
                    tree.append(node.left)
                if node.right:
                    tree.append(node.right)
            if len(temp) != 0:
                ret.append(temp)
            temp = []
            while tree:
                snode = tree.pop()
                if snode.right:
                    q.append(snode.right)
                if snode.left:
                    q.append(snode.left)
                temp.append(snode.val)
            if len(temp) != 0:
                ret.append(temp)
        return ret


b = Tree(7, None, None)
a = Tree(15, None, None)
left = Tree(9, None, None)
right = Tree(20, a, b)
root = Tree(3, left, right)

sol = Solution()
print(sol.zigzagLevelOrder(root))
