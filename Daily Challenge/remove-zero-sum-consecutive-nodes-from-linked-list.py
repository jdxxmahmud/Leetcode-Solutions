# Problem Link: https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list
# March 12, 2024

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        front = ListNode(0, head)
        startNode = front

        while startNode:
            sum = 0
            end = startNode.next

            while end:
                sum += end.val
                if sum == 0:
                    startNode.next = end.next
                end = end.next

            startNode = startNode.next


        return front.next
