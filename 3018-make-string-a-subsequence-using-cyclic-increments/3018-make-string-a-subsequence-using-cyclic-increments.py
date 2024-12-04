class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n, m = len(str1), len(str2)
        if m > n:
            return False
        
        s2 = 0  
        for char in str1:
            if s2 < m:
                next_char = chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
                if char == str2[s2] or next_char == str2[s2]:
                    s2 += 1  
            if s2 == m:
                return True
        
        return s2 == m
