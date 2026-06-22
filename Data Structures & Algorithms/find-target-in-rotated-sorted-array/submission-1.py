class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        
        while left < right:
            mid = left+(right-left)//2
            if nums[mid]< nums[right]:
                right=mid
            else :
                left=mid+1

        pivot = left

        def binary(left, right):
         while left <= right:          # ✅ 加上等號
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1        # ✅ 往右搜尋
            elif nums[mid] > target:
                right = mid - 1       # ✅ 往左搜尋
            else:
                return mid            # ✅ 找到了

         return -1    
        result=binary(0,pivot-1)
        if result != -1:
            return result
        else :
            return binary(pivot,len(nums)-1)

