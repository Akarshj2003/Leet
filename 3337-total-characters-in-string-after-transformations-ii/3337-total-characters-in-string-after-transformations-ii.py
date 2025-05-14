class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MOD = 10**9 + 7

        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1

        for _ in range(t):
            new_freq = [0] * 26
            for i in range(26):
                count = freq[i]
                if count == 0:
                    continue
                for j in range(1, nums[i] + 1):
                    new_char_index = (i + j) % 26
                    new_freq[new_char_index] = (new_freq[new_char_index] + count) % MOD
            freq = new_freq

        return sum(freq) % MOD