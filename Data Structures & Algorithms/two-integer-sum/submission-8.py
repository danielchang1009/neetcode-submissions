class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapval={}
        for i ,n in enumerate(nums):
            mapval[n] = i

        
        for i , n in enumerate(nums):
            diff = target-n
            if diff in mapval and mapval[diff]!=i:
                return [i , mapval[diff]]
        return []

