import math


class Solution:
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        dist = set()
        dist.add(self.findDistance(p1, p2))
        dist.add(self.findDistance(p1, p3))
        dist.add(self.findDistance(p1, p4))
        dist.add(self.findDistance(p2, p3))
        dist.add(self.findDistance(p3, p4))
        dist.add(self.findDistance(p2, p4))
        k = list(dist)
        print("Size =", len(dist))
        print(k[0], k[1])
        print(k[1] * math.sqrt(2))
        if len(dist) == 2 and ((k[0] * math.sqrt(2) == k[1]) or (k[1] * math.sqrt(2) == k[0])):
            print(True)
        print(False)

    def findDistance(self, p1, p2):
        return math.sqrt(((p1[0] - p2[0]) * (p1[0] - p2[0])) + ((p1[1] - p2[1]) * (p1[1] - p2[1])))

    def plusOne(self, A):
        hand = 1
        for i in range(len(A) - 1, -1, -1):
            if i == 0 and A[i] == 9 and hand == 1:
                A[i] = 0
                A.insert(0, 1)
                break
            if A[i] == 9 and hand == 1:
                A[i] = 0
                hand = 1
            elif i == len(A) - 1 and A[i] < 9:
                A[i] += 1
                hand = 0
                break
            else:
                A[i] += hand
                hand = 0
        return A


p1 = [0, 1]
p2 = [0, -1]
p3 = [1, 0]
p4 = [-1, 0]

sol = Solution()
sol.validSquare(p1, p2, p3, p4)
