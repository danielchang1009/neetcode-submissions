class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            n=len(nums)
            prefix=[0]*n
            postfix=[0]*n
            ans=[0]*n

            prefix[0] =1# 將 prefix[0] 初始化為 nums 的第一個元素
            postfix[n - 1] =1# 初始化 postfix 的最後一個元素
            for i in range(1,n):
                prefix[i]=prefix[i-1]*nums[i-1] # 計算累積乘積，包含 nums[i]
            

            for i in range(n - 2, -1, -1):
                postfix[i] = postfix[i+1] * nums[i+1]
            for i in range(n):
                ans[i]=prefix[i]*postfix[i]
            return ans

