from collections import deque
class Solution:
    def levelOrder(self, root):
        q = deque()
        tree=[]
        if not root:
            return tree
        q.append(root)
        while(q):
            k = len(q)
            temp =[]
            for i in range(k):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                temp.append(node)
            tree.append(temp)
        return temp