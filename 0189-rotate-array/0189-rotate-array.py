class Solution:
    def reverse(self,arr,start,end):
        while(start<end):
            arr[start],arr[end]=arr[end],arr[start]
            start+=1
            end-=1
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k=k%n
        self.reverse(nums,0,n-k-1)
        self.reverse(nums,n-k,n-1)
        self.reverse(nums,0,n-1)
        
        
    
        

    
    
        
        