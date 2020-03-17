class Solution:
    def checkPalindrome(self, s, left, right) -> bool:
        while left <= right:
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
                
        return True

    def validPalindrome(self, s: str) -> bool:
        if len(s) < 3:
            return True

        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                return self.checkPalindrome(s, left + 1, right) or self.checkPalindrome(s, left, right - 1)
            else:
                left += 1
                right -= 1
                
        return True


# It works for short strings, if input long strings, Time Limit Exceeded.
# O(N^2)

#  class Solution:
#     def checkPalindrome(self, s) -> bool:
#         if len(s) == 1: 
#             return True

#         left, right = 0, len(s) - 1
#         while left <= right:
#             if s[left] != s[right]:
#                 return False
#             else:
#                 left += 1
#                 right -= 1
                
#         return True

#     def validPalindrome(self, s: str) -> bool:
#         if len(s) == 1:
#             return True

#         ls = []
#         for c in s:
#             ls.append(c)

#         isPalindrome = False
#         for i in range(len(ls)):
#             sub = ls[:]
#             sub.pop(i)
#             isPalindrome = self.checkPalindrome(sub)
#             if isPalindrome:
#                 return True

#         return False      
