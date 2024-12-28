class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        values = {}
        for i, num in enumerate(nums):
            if num in values and i - values[num] <= k:
                return True
            values[num] = i # keep the last
        return False
        