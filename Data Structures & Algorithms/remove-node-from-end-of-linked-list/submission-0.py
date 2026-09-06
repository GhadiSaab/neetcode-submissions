# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        cur = head 
        counter = 0 
        while cur: 
            counter += 1
            cur = cur.next

        cur = head
        index = counter - n 

        counter = 0

        if index == 0:
            return head.next

        while cur:
            counter += 1
            if counter == index:
                prev = cur
            if counter == index+1:
                prev.next = cur.next

            cur = cur.next

        return head
