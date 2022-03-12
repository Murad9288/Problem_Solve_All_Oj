class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        # insert node copy right after the original one in the list
        current = head
        while current is not None:
            current.next = Node(current.val, next=current.next, random=current.random)
            current = current.next.next
            
        # since we know, that the copy is the next node after an original one,
        # the only thing we should do for clones is to shift it's
        # 'next' and 'random' pointers one node ahead
        current = head.next
        while current is not None:
            if current.next is not None:
                current.next = current.next.next

            if current.random is not None:
                current.random = current.random.next
            
            current = current.next
            
        return head.next
