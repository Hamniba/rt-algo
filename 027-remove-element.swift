class Solution {
    func removeElement(_ nums: inout [Int], _ val: Int) -> Int {
        var head = 0
        var tail = nums.count
        
        while head < tail {
            if nums[head] == val {
                let tmp = nums[tail - 1]
                nums[tail - 1] = nums[head]
                nums[head] = tmp
                
                tail -= 1
            }
            else {
                head += 1
            }
        }
        
        return tail
    }
}
