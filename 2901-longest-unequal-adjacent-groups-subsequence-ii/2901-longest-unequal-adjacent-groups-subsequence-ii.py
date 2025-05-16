class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n=len(words)
        parent=[-1]*n
        dp=[1]*n
        maxlen=1
        last_intex=0
        if n==1:
            return words
        def find_hamming_distance(w1,w2):
            distance=0
            for char1,char2 in zip(w1,w2):
                if char1!=char2:
                    distance+=1
            return distance
        for i in range(n):
            for j in range(i+1,n):
                if groups[i]!=groups[j] and len(words[i]) == len(words[j]):
                    if find_hamming_distance(words[i],words[j])==1:
                        if dp[i]+1 > dp[j]:
                            dp[j]=dp[i]+1
                            parent[j]=i
                            if dp[j] > maxlen:
                                maxlen=dp[j]
                                last_intex=j
        answer=[]
        while last_intex!=-1:
            answer.append(words[last_intex])
            last_intex=parent[last_intex]
        answer.reverse()
        return answer