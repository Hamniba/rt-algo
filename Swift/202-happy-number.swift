//
//  202-happy-number.swift
//
//  Created by Owen on 2019.
//

class Solution {
    func isHappy(_ n: Int) -> Bool {
        
        // 1.
        if n == 1 {
            return true
        }
        
        var nums = [Int: Int]()
        var sum = n
        
        while sum != 1 {
            // 2.
            if nums[sum] == nil {
                nums[sum] = 1
                var tmp = 0
                // 3.
                while sum != 0 {
                    tmp = tmp + (sum % 10) * (sum % 10)
                    sum = sum / 10
                }
                
                sum = tmp
            }
            else {
                return false
            }
        }
        
        return true
    }
}


/*
 问题：判断某个数是否是 Happy Number。
 
 判定 Happy Number 的规则：
 一个整数 N，把它每一位上的数字单独拆出来，并把这些数字各自的平方相加，结果为 M，接着把 M 拿来作上述拆解运算，循环这个过程，直到计算到 M = 1 为止，则判断算法的输入 N 为 Happy Number。
 不是 Happy Number 的情况：在不断拆解计算的循环过程中，若某个计算的结果值 M 出现了两次，再对这个重复的 M 作拆解计算，必然会再次计算得到这个 M 三次四次，在此情况下算法将进入无限死循环中，此时就可以判断该输入 N 不是 Happy Number。而要判断这个 M 是否重复出现过，就要用到 Hash Table 了。
 
 解：
 1. 考虑到边界条件，若输入为 1，直接判为 true
 2. 每一次拆解运算的循环开始，就先判断字典中是否存在这个值，没有就在字典中记录一下
 3. 对数字的字符拆解，还是用取模和除法运算来实现
 */
