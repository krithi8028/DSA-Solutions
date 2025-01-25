class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordcount=Counter(words)
        

        pq=[(-freq,char) for char,freq in wordcount.items()]
        heapq.heapify(pq)
        res=[]
        while k:
            freq,char=heapq.heappop(pq)
            res.append(char)
            k-=1

        return res


        