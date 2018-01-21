# def search( A, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: int
#     """
#     if len(A) == 0:
#         return -1
#     lo, hi = 0, len(A) - 1
#     pivot = 0
#     while lo < hi:
#         if hi == lo + 1 and A[hi] < A[lo]:
#             pivot = hi
#             print("pivot", pivot)
#             break
#         mid = (lo + hi) // 2
#         print(lo, hi, mid)
#         if A[hi] < A[mid]:
#             lo = mid
#         else:
#             hi = mid
#
#     print(lo, hi, pivot)
#     return None
#
# A= [1,3]
# inp = [ 101, 103, 106, 109, 158, 164, 182, 187, 202, 205, 2, 3, 32, 57, 69, 74, 81, 99, 100 ]
# search(A, 0)

class Solution:
	# @param A : tuple of integers
	# @return an integer
	def maximumGap(self, A):
        j = len(A)-1
	    leftmin =[]
	    rightmax= [-1 for i in range(0, len(A))]
        leftmin.append(A[0])
        for i in range(1, len(A)):
            leftmin.append(min(A[i],leftmin[i-1]))
        for i in range(j-1, -1,-1):
            rightmax[i] = max(A[i], rightmax[i+1])
        i = 0
        j = 0
        diff = -1
        while i<len(A) and j < len(A):
            if leftmin[i]<rightmax[j]:
                diff = max(diff, j-i)
                j+=1
            else:
                i+=1
        return diff