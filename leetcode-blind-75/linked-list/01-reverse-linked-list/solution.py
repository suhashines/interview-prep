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

    head = ListNode(arr[0])
    tmp = head

    for i in range (1,len(arr)):

        node = ListNode(arr[i])
        tmp.next = node
        tmp = node

    return head

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


arr = [1,2,3,4,5]
head = createList(arr)

printList(reverseList(None))