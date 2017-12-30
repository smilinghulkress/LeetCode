from collections import deque
class Solution:
    def rightSideView(self, root):
        res =[]
        q = deque()
        if not root:
            return []
        q.append(root)
        while(q):
            k = len(q)
            for i in range(q):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(node.val)

        return res
