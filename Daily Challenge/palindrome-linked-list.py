# Problem Link: https://leetcode.com/problems/palindrome-linked-list
# March 22, 2024

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        # go to middle 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse
        prev = None
        while slow:
            nex = slow.next
            slow.next = prev

            prev = slow
            slow = nex

        # compare
        while prev:
            if prev.val != head.val:
                return False

            head, prev = head.next, prev.next

        return True
