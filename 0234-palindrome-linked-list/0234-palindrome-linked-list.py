# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        pal = ""
        current = head
        while current.next:
            pal+=(str(current.val))
            current=current.next
        pal+=(str(current.val))
        if pal[:] == pal[::-1]:
            return True
        else:
            return False

