# Problem Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list
# Daily Problem March 3, 2024

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = ListNode(0, head)
        right = left

        head = left

        for _ in range(n + 1):
            right = right.next

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return head.next
