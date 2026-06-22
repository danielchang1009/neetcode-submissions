class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            while l < r:
                if nums[i]+nums[l]+nums[r]==0 :
                    s=[nums[i],nums[l],nums[r]]
                    s.sort()
                    if s not in res:
                        res.append(s)
                    l+=1
                    r-=1
                elif nums[i]+nums[l]+nums[r] <0:
                    l+=1
                elif nums[i]+nums[l]+nums[r] >0:
                    r-=1
        return res