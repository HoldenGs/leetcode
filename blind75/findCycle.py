class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: Optional[ListNode]) -> bool:
    fast = head
    slow = head
    while fast and slow:
        fast = fast.next
        if fast == slow and fast != None:
            return True
        
        slow = slow.next
        if fast != None:
            fast = fast.next
    
    return False