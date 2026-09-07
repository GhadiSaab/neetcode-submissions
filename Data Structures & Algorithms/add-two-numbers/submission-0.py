class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        hold = 0
        dummy = ListNode()
        head = dummy

        while l1 or l2:

            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            nodes_sum = v1 + v2 + hold
            hold = nodes_sum // 10
            nodes_sum = nodes_sum % 10

            dummy.next = ListNode(nodes_sum)
            dummy = dummy.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if hold:
            dummy.next = ListNode(hold)

        return head.next