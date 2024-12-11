class Solution(object):
    def getPermutation(self, n, k):
        fact=1
        num=[]
        ans=''
        for i in range(1,n):
            fact*=i
            num.append(i)
        num.append(n)
        k-=1
        while(True):
            
            ans+=str(num[k//fact])
            num.pop(k//fact)
            if not num:
                break
            k%=fact
            fact//=len(num)
        return ans