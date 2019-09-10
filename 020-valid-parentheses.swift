class Solution {
    func isValid(_ s: String) -> Bool {
        if s.count == 0 {
            return true
        }
        
        var stack = [Character]()
        var pair: Character?
        
        for c in s {
            if pair != c {
                stack.append(c)
                pair = getAnotherPair(c)
            }
            else {
                _ = stack.popLast()
                if let last = stack.last {
                    pair = getAnotherPair(last)
                }
                else {
                    pair = nil
                }
            }
        }
        
        if stack.count == 0 {
            return true
        }
        else {
            return false
        }
    }
    
    func getAnotherPair(_ c: Character) -> Character {
        var s = ""
        
        switch c {
        case "(":
            s = ")"
        case ")":
            s = "("
        case "{":
            s = "}"
        case "}":
            s = "{"
        case "[":
            s = "]"
        case "]":
            s = "["
        default:
            s = ""
        }
        
        return Character(s)
    }
}


/*
 解决方案 一
 利用栈这种数据结构来做。
 
 先准备三组匹配的括号 [] {} ()
 声明一个数组作为栈 stack = []()
 
 首先判断特殊情况，输入字符串为空，return true
 
 for loop 遍历输入的字符串 {
    判断当前字符 c 是否与栈顶的字符相匹配（不是相等）
     if 不匹配 {
        将 c 入栈
        同时得到与 c 对应的另一个字符，用于下一次遍历做比较
     }
     else 匹配 {
        弹出栈顶字符
        if 如果此时栈不为空 {
            保存与当前栈顶字符相匹配的另一个字符，用于下一次遍历比较
        }
        else 栈为空 {
            用于下次遍历比较的字符 = nil
        }
     }
 }
 
整个字符串遍历结束之后，if 栈为空 return true 否则 return false
 
 */
