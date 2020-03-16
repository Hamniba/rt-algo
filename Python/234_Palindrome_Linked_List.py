# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        while len(stack) > 1:
            if stack[0] != stack[-1]:
                return False
            else:
                stack.pop(0)
                stack.pop()

        return True


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2

    print(Solution().isPalindrome(node1))
        