//
//  013-roman-to-integer.swift
//
//  Created by Owen on 2019.
//

class Solution {
    func romanToInt(_ s: String) -> Int {
        
        let patterns: [Character: Int] = ["I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000]
        var sum = 0
        var nums = [Int]()
        
        // 1.
        for (_, c) in s.enumerated() {
            if let num = patterns[c] {
                nums.append(num)
            }
        }
        
        // 2.
        while nums.count != 0 {
            if nums.count == 1 {
                sum += nums[0]
                nums.removeFirst()
            }
            else if nums[0] >= nums[1] {
                sum += nums[0]
                nums.removeFirst()
            }
            else {
                sum = sum + (nums[1] - nums[0])
                nums.removeFirst()
                nums.removeFirst()
            }
        }
        
        return sum
    }
}


/*
 问题：把罗马数字转换成阿拉伯数字。
 
 罗马数字用符号 I, V, X, L, C, D, M 表示，分别对应阿拉伯数字的值如上 patterns 所示。
 用罗马数字表示的规则如下：
 从左往右，如果前一个字符所代表的数值大于等于后一个字符，则字符所对应的数值应直接做加法；
 如果前一个字符所代表的数值小于后一个字符，这两个字符组合在一起代表的数值为后者减去前者。
 比如 "III" = 3, "IV" = 4, "VI" = 6
 
 解法：
 1. 把输入的罗马字符串的每个字符所对应的数值按顺序存储到数组中
 2. 遍历数组，按以上规则作对应的加减法计算，然后把计算过的值从该数组中移除，直到数组清空为止
 */
