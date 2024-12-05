class Solution(object):
    def combinationSum2(self, candidates, target):
        curr=[]
        ans=[]
        candidates.sort()
        def subseq(index,target):
            if target==0:
                ans.append(curr[:])
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                curr.append(candidates[i])
                subseq(i+1,target-candidates[i])
                curr.pop()
        subseq(0,target)
        return ans

        