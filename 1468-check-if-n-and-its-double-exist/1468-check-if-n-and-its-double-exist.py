class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        mp={}

        for i in range(len(arr)):
            if arr[i]*2 in mp or arr[i]/2 in mp:
                return True    
            mp[arr[i]]=1+mp.get(arr[i],0)
        return False

        