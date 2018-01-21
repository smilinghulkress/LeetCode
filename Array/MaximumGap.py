class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):

        j = len(A) - 1
        leftmin = []
        rightmax = [-1 for i in range(0, len(A))]
        leftmin.append(A[0])
        rightmax[j]= A[j]
        for i in range(1, len(A)):
            leftmin.append(min(A[i], leftmin[i - 1]))
        for i in range(j - 1, -1, -1):
            rightmax[i] = max(A[i], rightmax[i + 1])
        print(leftmin)
        print("RIght", rightmax)
        i = 0
        j = 0
        diff = -1
        while i < len(A) and j < len(A):
            if leftmin[i] < rightmax[j]:
                diff = max(diff, j - i)
                j += 1
            else:
                i += 1
        return diff

A= [1,10]
sol = Solution()
print(sol.maximumGap(A))
