# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        if head.next == None:
            return head
        current = head
        x = 0
        while current.next != None:
            x=x+1
            current = current.next
        current2 = head
        i=0
        while current2.next != None:
            current2=current2.next
            i=i+1
            if x % 2 == 1:
                if i == (x//2)+1:
                    return current2
            else:
                if i == ((x//2)):
                    return current2

        
