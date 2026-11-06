# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        vals = []
        if current == None:
            return False
        while current.next != None:
            vals.append(current)
            current = current.next
            i = 0
            for i in range(len(vals)):
                if vals[i] == current:
                    return True
        return False