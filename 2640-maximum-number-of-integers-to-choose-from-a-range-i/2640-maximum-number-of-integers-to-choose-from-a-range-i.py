class Solution(object):
    def maxCount(self, banned, n, maxSum):
        """
        :type banned: List[int]
        :type n: int
        :type maxSum: int
        :rtype: int
        """
        bannedset=set(banned)
        summ=0
        count=0

        for i in range(1,n+1):
            if i in bannedset:
                continue
            summ+=i
            if summ>maxSum:
                break
            count+=1
        return count