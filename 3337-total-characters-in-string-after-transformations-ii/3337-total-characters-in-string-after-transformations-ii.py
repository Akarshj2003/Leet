class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MOD = 10**9 + 7
        def mat_mult(A, B):
            res = [[0] * 26 for _ in range(26)]
            for i in range(26):
                for k in range(26):
                    if A[i][k]:
                        for j in range(26):
                            res[i][j] = (res[i][j] + A[i][k] * B[k][j]) % MOD
            return res

        def mat_pow(mat, power):
            res = [[int(i == j) for j in range(26)] for i in range(26)]  # Identity matrix
            while power:
                if power % 2:
                    res = mat_mult(res, mat)
                mat = mat_mult(mat, mat)
                power //= 2
            return res

        # Step 1: Transition matrix
        M = [[0] * 26 for _ in range(26)]
        for i in range(26):
            for j in range(1, nums[i] + 1):
                M[i][(i + j) % 26] += 1

        # Step 2: Initial frequency vector
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1

        # Step 3: Matrix exponentiation
        M_pow = mat_pow(M, t)

        # Step 4: Multiply initial vector by the matrix
        result = [0] * 26
        for i in range(26):
            for j in range(26):
                result[j] = (result[j] + freq[i] * M_pow[i][j]) % MOD

        return sum(result) % MOD