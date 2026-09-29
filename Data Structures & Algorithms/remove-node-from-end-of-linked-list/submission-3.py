# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        len_list = 0
        cur = head

        while cur: 
            len_list += 1
            cur = cur.next

        index = len_list - n

        dummy = ListNode()
        dummy.next = head
        cur = dummy 
        counter = 0 
        while counter < index:
            counter += 1
            cur = cur.next

        cur.next = cur.next.next


        return dummy.next 




