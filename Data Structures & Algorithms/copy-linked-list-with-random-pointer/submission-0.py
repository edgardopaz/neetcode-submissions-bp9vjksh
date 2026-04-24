"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        dicti = {None: None}
        
        ptr = head
        prev = None
        new_head = None
       
        while ptr:
            new_node = Node(ptr.val)
            if not new_head:
                new_head = new_node
            dicti[ptr] = new_node
            if prev:
                prev.next = new_node
            ptr = ptr.next
            prev = new_node
            
        ptr = head
        new_ptr = new_head
        
        while ptr:
            new_ptr.random = dicti[ptr.random]
            ptr = ptr.next
            new_ptr = new_ptr.next
            
        return new_head 