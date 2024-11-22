class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        pat_freq = Counter()
        
        for r in matrix:
            pattern = tuple(r) if r[0] == 0 else tuple(bit ^ 1 for bit in r)
            pat_freq[pattern] += 1
            
        return max(pat_freq.values())