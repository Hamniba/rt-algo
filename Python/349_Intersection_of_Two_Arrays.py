class Solution:
    def intersection_in_set(self, set1, set2):
        result = []
        
        for x in set1:
            if x in set2:
                result.append(x)
                
        return result
    
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        
        if len(set1) < len(set2):
            return self.intersection_in_set(set1, set2)
        else:
            return self.intersection_in_set(set2, set1)
            
            
    
                
        