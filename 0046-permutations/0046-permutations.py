class Solution(object):
    def permute(self, nums):
        #Recursive code
        
        ans = []


        def subseq(index):
            if index==len(nums):
                ans.append(nums[:])
                return 
            for i in range(index,len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                subseq(index + 1)
                nums[index], nums[i] = nums[i], nums[index]
            
        subseq(0)
        return ans
        