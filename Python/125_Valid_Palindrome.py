class Solution:
    # s 字符串只需要字母和数字，不包括符号和空格
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True

        alpha = set('abcdefghijklmnopqrstuvwxyz1234567890')
        ls = []
        for c in s:
            if c.lower() in alpha:
                ls.append(c.lower())

        if len(ls) == 1:
            return True

        start, end = 0, len(ls)-1    

        while start <= end:
            if ls[start] != ls[end]:
                return False
            else:
                start += 1
                end -= 1
            
        return True

if __name__ == '__main__':
    s = Solution()
    r = s.isPalindrome("0p")
    print(r)


