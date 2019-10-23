class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        d = {}
        for i in range(len(nums1)):
            if not d.get(nums1[i]):
                d[nums1[i]] = 1
        i, j = 0, len(nums2) - 1
        while i <= j:
            if d.get(nums2[i]):
                d[nums2[i]] -= 1
                i += 1
            else:
                nums2[i], nums2[j] = nums2[j], nums2[i]
                j -= 1

        return nums2[:i]

