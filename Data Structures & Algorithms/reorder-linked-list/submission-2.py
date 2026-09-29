# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # get the middle node
        dummy = ListNode()
        dummy.next = head
        slow = fast = dummy
        count = 0

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        def reverselist(head):
            prev = None
            cur = head 
            while cur: 
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            return prev

        midhead = reverselist(slow.next)
        slow.next = None

        dummy = ListNode()
        dummy.next = head
        cur = dummy
        finalhead = dummy
        
        while head and midhead:
            if count == 0:
                cur.next = head
                count += 1
                head = head.next
            elif count == 1:
                cur.next = midhead
                count -= 1
                midhead = midhead.next

            cur = cur.next

        if head is not None: cur.next = head
        if midhead is not None: cur.next = midhead


            
        