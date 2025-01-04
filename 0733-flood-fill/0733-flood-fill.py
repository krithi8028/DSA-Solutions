class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n=len(image)
        m=len(image[0])
        directions=[[-1,0],[0,-1],[1,0],[0,1]]
        q=deque()
        ans=image
        initial=image[sr][sc]
        ans[sr][sc]=color
        q.append((sr,sc))
        while q:
            curr=q.popleft()
            r=curr[0]
            c=curr[1]
            for i in range(len(directions)):
                nr=r+directions[i][0]
                nc=c+directions[i][1]
                if nr>=0 and nr<n and nc>=0 and nc<m and image[nr][nc]==initial and ans[nr][nc]!=color:
                    q.append((nr,nc))
                    ans[nr][nc]=color
        return ans

        