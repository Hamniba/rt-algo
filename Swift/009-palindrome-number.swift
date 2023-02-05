//
//  009-palindrome-number.swift
//
//  Created by Owen on 2019.
//

class Solution {
    func isPalindrome(_ x: Int) -> Bool {
        // 1.
        if x < 0 {
            return false
        }
        if x == 0 {
            return true
        }
        
        // 2.
        var digits = [Int]()
        var y = x
        while y != 0 {
            digits.append(y % 10)
            y = y / 10
        }
        
        // 3.
        var result = true
        if digits.count % 2 == 0 {
            let n = digits.count/2 - 1
            for i in 0...n {
                if digits[i] != digits[digits.count - i - 1] {
                    result = false
                    break
                }
            }
        }
        else {
            let n = digits.count/2
            for i in 0..<n {
                if digits[i] != digits[digits.count - i - 1] {
                    result = false
                    break
                }
            }
        }
        
        
        return result
    }
}


/*
 1. 由题目可排除负数肯定不是 Palindrome(回文)，0 是。
 2. 题目不允许将输入 x 转换成字符串，那就通过取模的方式将 x 的每一个数字按顺序存储到一个数组中。
 3. 只需要遍历一半这个数组，检查数组是否是对称的，如果每个数字都关于数组中间的位置对称，则判断 x 是回文。
 */
