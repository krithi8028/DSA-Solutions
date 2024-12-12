class Solution(object):
    def permute(self, nums):
        #Recursive code
        stack = []
        mapp = {num: 0 for num in nums} 
        ans = []


        def subseq(stack,mapp):
            if len(stack)==len(nums):
                ans.append(stack[:])
                return 
            for i in nums:
                if mapp[i]==0:
                    mapp[i]=1
                    stack.append(i)
                    subseq(stack,mapp)
                    stack.pop()
                    mapp[i]=0
            
            
            
            
            

        subseq(stack,mapp)
        return ans
        