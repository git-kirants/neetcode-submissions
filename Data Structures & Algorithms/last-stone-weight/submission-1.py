class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = stones
        heap = [-x for x in heap]
        heapq.heapify(heap)
        while len(heap)>1:
            f = -heapq.heappop(heap)
            s = -heapq.heappop(heap)
            if f != s:
                heapq.heappush(heap, -(f-s))
                
        heap = [-x for x in heap]
        if heap:
            return heap[0]
        else:
            return 0

