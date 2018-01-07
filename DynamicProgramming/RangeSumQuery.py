class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.suma = []
        self.suma.append(nums[0])
        for i in range(1, len(nums)):
            self.suma.append(nums[i] + self.suma[i - 1])

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if len(nums)==0:
            return 0
        print(self.suma)
        print((self.suma[i], self.suma[i-1])[i > 0])
        return self.suma[j] - (0, self.suma[i-1])[i > 0]

nums = [-2, 0, 3, -5, 2, -1]
numa = NumArray(nums)
print(numa.sumRange(0,2))
