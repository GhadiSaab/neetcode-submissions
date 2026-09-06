# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ## find the middle of the linked list
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head_2 = slow.next
        slow.next = None

        ## reversing the second list

        cur = head_2
        prev = None

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur 
            cur = nxt 

        head_2 = prev

        ## merging the 2 list

        dummy = ListNode()

        while head and head_2:
            dummy.next = head
            head = head.next
            dummy = dummy.next
            dummy.next = head_2
            head_2 = head_2.next
            dummy = dummy.next

        if head:
            dummy.next = head
        if head_2:
            dummy.next = head_2

