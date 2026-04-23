# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return 
        dummy = ListNode(0, head)
        first, second = dummy, head

        for _ in range(1, n):
            second = second.next

            if second is None:
                return -1
        
        while second.next is not None:
            second = second.next
            first = first.next
        
        first.next = first.next.next

        return dummy.next