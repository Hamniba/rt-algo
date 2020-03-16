class Solution:
    def findPalindrome(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left+1 : right]

    def longestPalindrome(self, s: str) -> str:
        palindrome = ''
        for i in range(len(s)):
            s1 = self.findPalindrome(s, i, i)  # odd palindrome
            s2 = self.findPalindrome(s, i, i + 1)  # even palindrome
            if len(palindrome) < len(s1):
                palindrome = s1
            
            if len(palindrome) < len(s2):
                palindrome = s2

        return palindrome


if __name__ == '__main__':
    s = 'cbbd'
    o = Solution().longestPalindrome(s)
    print(o)