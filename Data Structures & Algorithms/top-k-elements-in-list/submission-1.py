class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for element in nums:
              dic[element]=dic.get(element,0)+1
        sorted_dic=sorted(dic.items(), key=lambda item: item[1], reverse=True)
        return[num for num,j in sorted_dic[:k] ]
              