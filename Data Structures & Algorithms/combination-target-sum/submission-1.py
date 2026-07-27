class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        nums.sort()
        def dfs(idx,path, cur):
            if cur == target: 
                res.append(path.copy())
                return 
            for i in range(idx, len(nums)):
                if cur + nums[i] > target:
                    break 
                path.append(nums[i])
                dfs(i, path, cur+nums[i])
                path.pop()
        dfs(0,[],0)
        return res