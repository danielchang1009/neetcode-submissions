class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
     dic = defaultdict(list)
     for s in strs:
        sorteds=''.join(sorted(s))
        dic[sorteds].append(s)
     return list(dic.values())