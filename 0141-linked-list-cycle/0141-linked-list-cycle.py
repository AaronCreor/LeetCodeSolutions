# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        vals = set()
        if current == None:
            return False
        while current.next != None:
            if current in vals:
                return True
            vals.add(current)
            current = current.next
        return False