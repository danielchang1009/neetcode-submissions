class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        data = [-i for i in nums]
        heapq.heapify(data)
        while len(data) > 1 and k > 1 : 
            first = heapq.heappop(data)
            second = heapq.heappop(data)
            if first <= second :
                heapq.heappush(data, second)
                k-=1 
            else:
                temp = first 
                first = second 
                second = temp
                heapq.heappush(data, second)
                heapq.heappush(data, first)


        data.append(0)
        return -data[0]
            