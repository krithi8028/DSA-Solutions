class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        score = 0
        idx = values[0]
        for i in range(1, len(values)):
            idx -= 1
            j = values[i]
            score = max(score, idx + j)
            idx = max(idx, j)
        return score