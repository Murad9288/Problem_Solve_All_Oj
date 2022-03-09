class Solution(object):
    def deleteDuplicates(self, head):
        if head == None or head.next == None:  
            return head
        if head.val == head.next.val and head.next.next == None:
            return None
        if head.val != head.next.val:  
            head.next = self.deleteDuplicates(head.next)
            return head
        if head.next.next != None and head.next.val != head.next.next.val:
            return self.deleteDuplicates(head.next.next)
        return self.deleteDuplicates(head.next)
