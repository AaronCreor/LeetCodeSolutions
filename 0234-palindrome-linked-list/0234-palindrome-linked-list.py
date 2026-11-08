# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        current = head
        stackL = deque()
        stackR = deque()
        while current.next:
            stackL.appendleft(current.val)
            stackR.append(current.val)
            current=current.next
        stackL.appendleft(current.val)
        stackR.append(current.val)
        if stackL == stackR:
            return True
        else:
            return False
        


