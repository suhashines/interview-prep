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

def merge_lists(list1,list2):

    dummy = ListNode(-1)

    l,r = list1,list2

    tmp = dummy

    while l and r:

        if l.val <= r.val:
            tmp.next = l
            l = l.next
        else:
            tmp.next = r
            r = r.next

        tmp = tmp.next
    
    while l:
        tmp.next = l
        l = l.next
        tmp = tmp.next
    while r:
        tmp.next = r
        r = r.next
        tmp = tmp.next
    
    head = dummy.next
    dummy = None
    return head

arr1 = [1,2,4]
list1 = createList(arr1)
arr2 = [1,3,4]
list2 = createList(arr2)

printList(merge_lists(list1,list2))