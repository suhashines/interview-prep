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

def merge_k_lists(lists):

    if len(lists) == 0:
        return None

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

    def recursive_merge(l,h):
        if l == h:
            # I have only one list, then it's already sorted
            return lists[l]
        m = (l+h)/2

        head1 = recursive_merge(l,m)
        head2 = recursive_merge(m+1,h)
        return merge_lists(head1,head2)
    
    return recursive_merge(0,len(lists)-1)



lists = [[1,4,5],[1,3,4],[2,6]]

lists = [[]]

linked_lists = [createList(i) for i in lists]

printList(merge_k_lists(linked_lists))