# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             s = target - nums[i]
#             for idx in range(i, len(nums)):
#                 if s == nums[idx]:
#                     return [i, idx]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            sub = target - nums[i]
            if sub in dic:
                return [i, dic[sub]]
            else:
                dic[nums[i]] = i


            
