class Solution:

    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def solve(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        decreased = True
        while i >= 0:
            if nums[i] < nums[i+1]:
                decreased = False
                break
            i -= 1
        start = i
        if decreased:
            for i in range(int(len(nums)/2)):
                self.swap(nums, i, len(nums) -1 - i)
            return
        base = nums[start]
        _min = len(nums) - 1
        for i in range(start + 1, int((start + len(nums) + 1)/2)):
            self.swap(nums, i, len(nums) - i + start)
        for i in range(start + 1, len(nums)):
            if nums[i] > base and nums[i] < nums[_min]:
                _min = i
            if nums[i] > base and nums[i] == nums[_min]:
                _min = min(i, _min)
        self.swap(nums, _min, start)