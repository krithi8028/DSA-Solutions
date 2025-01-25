class Solution:
    def frequencySort(self, s: str) -> str:
        wordcount=Counter(s)
        pq=[(-freq,char) for char,freq in wordcount.items()]
        heapq.heapify(pq)
        result=''
        while(pq):
            freq,char=heapq.heappop(pq)
            result+=(char*-freq)
        return result

        