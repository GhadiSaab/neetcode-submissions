class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None : return list2
        if list2 is None : return list1

        if  list1.val <= list2.val:
            start = list1
            head =list1
            list1 = list1.next
        else:
            start = list2
            head= list2
            list2 = list2.next

        while list1 and list2:
            if list1.val <= list2.val:
                start.next = list1
                list1 = list1.next
            else:
                start.next = list2
                list2 = list2.next

            start = start.next

        if list1 is not None: start.next = list1
        if list2 is not None: start.next = list2


        return head