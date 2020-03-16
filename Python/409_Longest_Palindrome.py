class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 0:
            return 0

        dic = {}
        for c in s:
            if dic.get(c):
                dic[c] += 1
            else:
                dic[c] = 1

        length = 0
        for n in dic.values():
            if n % 2 == 0:
                length += n
            else:
                length += (n//2) * 2

        if len(s) == length:
            return length
        else:
            return length + 1    

            

if __name__ == '__main__':
    print(Solution().longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"))



# 1. 给每个字符出现的次数计数
# 2. 出现偶数次的，可以全部拿来配对使用，length 直接加上它的数目
# 3. 出现奇数次的，其中的 n-1 个字符可以拿来配对使用，所以需要 length + (n//2)*2  # // 向下取整
# 4. 最后总的 length 与 s 长度相等，说明 s 里面的字符都出现了偶数次，否则至少有一个落单的字符，加上其中的一个就可以形成回文