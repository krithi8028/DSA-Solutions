class Solution(object):
    def findScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited=[False]*len(nums)
        arr=[]
        score=0

        for i,num in enumerate(nums):
            heappush(arr,(num,i))
        while arr:
            val,index=heappop(arr)
            if visited[index]!=True:
                score+=val
                visited[index]=True
            else:
                continue
            if index<len(nums)-1:
                visited[index+1]=True
            if index>0:
                visited[index-1]=True
        return score

            


