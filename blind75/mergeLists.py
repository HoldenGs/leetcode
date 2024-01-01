def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    merged_head = None
    merged_curr = None
    while list1 and list2:
        if list1.val <= list2.val:
            if merged_curr:
                merged_curr.next = list1
                merged_curr = list1
                list1 = list1.next
            else:
                merged_head = list1
                merged_curr = list1
                list1 = list1.next
                merged_curr.next = None
            
            
        else:
            if merged_curr:
                merged_curr.next = list2
                merged_curr = list2
                list2 = list2.next
            else:
                merged_head = list2
                merged_curr = list2
                list2 = list2.next
                merged_curr.next = None
            
        print(merged_curr.val)

    if list1 != None:
        if merged_curr:
            merged_curr.next = list1
        else:
            merged_head = list1
    elif list2 != None:
        if merged_curr:
            merged_curr.next = list2
        else:
            merged_head = list2

    return merged_head