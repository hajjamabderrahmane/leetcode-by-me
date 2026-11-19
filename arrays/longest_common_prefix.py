class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        s = ''
        k=0
        for a in strs[0]:
            for j in range(1,len(strs)):
            
                if len(strs[j]) <= k :
                    return s

                if a!= strs[j][k] :
                    return s
            k+=1
            s+=a
        return s
        

        