class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        result=0
        n=len(arr)
        for i in range(1,n-1):
            if arr[i-1]<arr[i]>arr[i+1]:
                l=r=i
                while l>0 and arr[l-1]<arr[l]:
                    l-=1
                while r+1<n and arr[r]>arr[r+1]:
                    r+=1
                result=max(result,(r-l+1))
        return result 