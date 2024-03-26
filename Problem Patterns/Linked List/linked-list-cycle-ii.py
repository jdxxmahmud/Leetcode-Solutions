# Problem Link: https://leetcode.com/problems/linked-list-cycle-ii

#Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                break

        slow2 = head

        while slow.next and slow2.next:

            if slow == slow2:
                return slow

            slow = slow.next
            slow2 = slow2.next

            

        return None

