# Problem Link: https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        root = ListNode()
        curr = root

        def merger(list1, list2, curr):

            if not list1 and not list2:
               return root.next

            if not list1:
                curr.next = list2
                return root.next

            if not list2:
                curr.next = list1
                return root.next

            if list1.val > list2.val:
                temp = ListNode(list2.val)
                list2 = list2.next
            else:
                temp = ListNode(list1.val)
                list1 = list1.next

            curr.next = temp

            return merger(list1, list2, curr.next)

        return merger(list1, list2, curr)
