class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        minv=min(abs(value) for row in matrix for value in row)
        n_values = [value for row in matrix for value in row if value < 0]
        if not len(n_values)&1:
            return sum(abs(value)for row in matrix for value in row)
        return sum(abs(value)for row in matrix for value in row)-(minv*2)
        