class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        arr=[]
        ans=[]
        def candidatesum(index,target):
            if index==len(candidates):
                if target ==0:
                    ans.append(arr[:])
                return 
            if candidates[index]<=target:
                arr.append(candidates[index])
                candidatesum(index,target-candidates[index])
                arr.pop()
            candidatesum(index+1,target)
            
        candidatesum(0,target)
        return ans

        

