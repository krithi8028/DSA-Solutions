class Solution(object):
    def binarysearch(self,nums, low , high , target):
        if low>high:
            return -1
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        elif target>nums[mid]:
            return self.binarysearch(nums,mid+1,high,target)
        return self.binarysearch(nums,low,mid-1,target)
    def search(self, nums, target):
        return self.binarysearch(nums,0,len(nums)-1,target)
        