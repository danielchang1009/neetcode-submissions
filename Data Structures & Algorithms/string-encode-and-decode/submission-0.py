class Solution:

    def encode(self, strs: List[str]) -> str:
        res=[]
        for s in range(len(strs)):
         encoded=str(len(strs[s]))+"#"+strs[s]
         res.append(encoded)
         
        return "".join(res)
    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i < len(s):
            j=i
            while s[j]!="#" :
                j+=1
            length=int(s[i:j])
            word=s[j+1:j+1+length]
            res.append(word)
            i=j+1+length
        return res