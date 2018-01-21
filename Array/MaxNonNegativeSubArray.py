class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        slen = 0
        sindex = 0
        subarray = []
        maxsum = 0
        temp = []
        tindex = 0
        tlen = 0
        tsum = 0
        for i in range(0, len(A)):
            if A[i] < 0:
                tindex = i - tlen
                print(A[i],temp,tsum, maxsum, subarray)
                if maxsum > tsum:
                    temp = []
                    tindex = 0
                    tlen = 0
                    tsum = 0
                elif maxsum < tsum:
                    slen = tlen
                    sindex = tindex
                    subarray = temp
                    maxsum = tsum
                    print("m<t", subarray, temp)
                    temp = []
                    tindex = 0
                    tlen = 0
                    tsum = 0
                else:
                    if slen > tlen:
                        temp = []
                        tindex = 0
                        tlen = 0
                        tsum = 0
                    elif slen < tlen:
                        slen = tlen
                        sindex = tindex
                        subarray = temp
                        maxsum = tsum
                        temp = []
                        tindex = 0
                        tlen = 0
                        tsum = 0
                    else:
                        if sindex > tindex:
                            temp = []
                            tindex = 0
                            tlen = 0
                            tsum = 0
                        else:
                            slen = tlen
                            sindex = tindex
                            subarray = temp
                            maxsum = tsum
                            temp = []
                            tindex = 0
                            tlen = 0
                            tsum = 0
            else:
                # print("Positive")
                temp.append(A[i])
                # print(temp)
                tlen += 1
                tsum += A[i]

        return subarray

# A = [ 1, 2, 5, -7, 2, 5 ]
sol = Solution()
A = [ 336465782, -278722862, -2145174067, 1101513929, 1315634022, -1369133069, 1059961393, 628175011, -1131176229, -859484421 ]
print("A:", A)

print("Solution ==", sol.maxset(A))