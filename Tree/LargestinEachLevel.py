from collections import deque
class Solution:
    def largestValues(self, root):
        q = deque()
        avg =[]
        if not root:
            return None
        q.append(root)
        while q:
            k = len(q)
            tempmax = float('-inf')
            for i in range(k):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                tempmax = max(tempmax,node.val)
            avg.append(tempmax)
        return avg
