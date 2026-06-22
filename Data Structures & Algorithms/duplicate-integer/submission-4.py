class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
     for i in range(len(nums)):
        for j in range(1+i,len(nums)):
            if  nums[i]==nums[j] :
               return True 
            
     return False