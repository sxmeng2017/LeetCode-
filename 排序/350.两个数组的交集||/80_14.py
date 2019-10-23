class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        n1, n2 = 0, 0
        res = []
        while n1 < len(nums1) and n2 < len(nums2):
            if nums1[n1] == nums2[n2]:
                res.append(nums1[n1])
                n1 += 1
                n2 += 1
            elif nums1[n1] < nums2[n2]:
                n1 += 1
            else:
                n2 += 1
        return res