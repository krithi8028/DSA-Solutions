class Solution(object):
    def maximumBeauty(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        i = 0
        for j in range(len(nums)):
            if nums[j] - nums[i] > k * 2:
                i += 1
        return j - i + 1