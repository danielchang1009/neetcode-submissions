class Solution:
    def maxArea(self, heights: List[int]) -> int:
        front , back = 0 ,len(heights)-1
        ans=0
        while front < back :
            area =  min(heights[back],heights[front] )*(back-front) 
            ans  =  max(ans,area)
            if  heights[front] <= heights[back] :
                front+=1
            else:
                back-=1
        return ans        
