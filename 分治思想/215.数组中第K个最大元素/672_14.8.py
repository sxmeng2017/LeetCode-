class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        self.buildheap(heap, k)
        for i in range(k, len(nums)):
            num = nums[i]
            if num > heap[0]:
                heap[0] = num
                self.buildheap(heap, k)
        return heap[0]

    def buildheap(self, heap, k):
        for i in reversed(range(k // 2)):
            self.heap(i, k, heap)

    def heap(self, i, n, heap):
        left, right = 2 * i + 1, 2 * i + 2
        min = i
        if left < n and heap[left] < heap[i]:
            heap[left], heap[i] = heap[i], heap[left]
            min = left
        if right < n and heap[right] < heap[i]:
            heap[right], heap[i] = heap[i], heap[right]
            min = right
        if min != i:
            self.heap(min, n, heap)