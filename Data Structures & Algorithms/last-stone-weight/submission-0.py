class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        data = [-i for i in stones]
        heapq.heapify(data)
        while len(data) > 1 :
            first = heapq.heappop(data)
            second = heapq.heappop(data)
            if  first < second :
                heapq.heappush(data,first-second)
        data.append(0)
        return abs(data[0])
