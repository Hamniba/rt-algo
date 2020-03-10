class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        dic = {}

        for n in nums1:
            if n in dic:
                dic[n] = dic[n] + 1
            else:
                dic[n] = 1

        for n in nums2:
            if n in dic and dic[n] > 0:
                result.append(n)
                dic[n] = dic[n] - 1

        return result