class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        data = [-i for i in nums]
        heapq.heapify(data)
        for i in range(k-1):
            heapq.heappop(data)
        data.append(0)
        return -data[0]