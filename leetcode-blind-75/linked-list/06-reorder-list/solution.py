class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printList(head):
     # print the list

    tmp = head

    while tmp:
        print(f"{tmp.val}->",end="")
        tmp = tmp.next

def createList(arr):

    if len(arr) == 0:
        return None
    
    head = ListNode(arr[0])
    tmp = head

    for i in range (1,len(arr)):

        node = ListNode(arr[i])
        tmp.next = node
        tmp = node

    return head

def reorderlist(head):

    if not head:
        return None
    
    slow = head
    fast = head.next

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    # after this loop the slow pointer is at the middle of the list
    # so we want to reverse the list after slow
    def reverseList(head:ListNode):

        if not head:
            return None
        
        tmp = None

        while head:
            next = head.next
            head.next = tmp
            tmp = head
            head = next
        return tmp

    left = head
    right = reverseList(slow.next)
    # since slow is at the middle of the list, it will be at the end after reordering
    # so we set slow.next as null
    slow.next = None

    while left and right:

        tl = left.next
        left.next = right
        tr = right.next
        right.next = tl
        right = tr
        left = tl
    return head

a = []

printList(reorderlist(createList(a)))


