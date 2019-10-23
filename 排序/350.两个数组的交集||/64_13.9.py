from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1, d2 = {}, {}
        for i in nums1:
            if not d1.get(i):
                d1[i] = 1
            else:
                d1[i] += 1
        for j in nums2:
            if not d2.get(j):
                d2[j] = 1
            else:
                d2[j] += 1
        res = []
        for (key, value) in d1.items():
            if key in d2.keys():
                m = min(d1[key], d2[key])
                for i in range(m):
                    res.append(key)
        return res