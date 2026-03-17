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

def remove_node(head,n):

    # the idea is to maintain a offset of n between fast and slow pointer

    if not head:
        return None
    
    dummy = ListNode(-1)
    dummy.next = head

    slow,fast = dummy,head

    for i in range(n):
        fast = fast.next

    while fast:

        slow = slow.next
        fast = fast.next

    # after this loop slow points to the previous of the targeted element
    slow.next = slow.next.next
    head = dummy.next
    dummy = None
    return head 