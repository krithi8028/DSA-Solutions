class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen=set()
        for index,value in enumerate(nums):
            if value in seen:
                return True
            seen.add(value)
            if len(seen)>k:
                seen.remove(nums[index-k])
        return False
        