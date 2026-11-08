# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return head
        curr = head
        prev = None
        next = curr.next
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev



            