class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        m = res

        while l1 or l2:
            if l1 is None:
                m.next =l2
                break
            elif l2 is None:
                m.next = l1
                break

            elif l1.val <= l2.val:
                m.next = l1
                l1 = l1.next
            else:
                m.next = l2
                l2 = l2.next
            m = m.next

        return res.next
