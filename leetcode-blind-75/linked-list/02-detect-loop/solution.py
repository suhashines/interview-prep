class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList(head,pos):
     # print the list

    tmp = head
    i = 0
    back = None

    while tmp and tmp.next != back:

        print(f"{tmp.val}->",end="")
        if i == pos:
            back = tmp
        tmp = tmp.next
        i += 1

    print(f"{tmp.val}",end="")

    if not back:
        return
    
    print(f"->{back.val}")

def createLoopList(arr,pos):

    head = ListNode(arr[0])
    tmp = head
    back = None

    for i in range (1,len(arr)):
        node = ListNode(arr[i])

        if i == pos:
            back = node

        tmp.next = node
        tmp = node

        if i == len(arr)-1:
            tmp.next = back

    return head

def has_loop(head):
    
    visited = {}

    tmp = head

    while tmp:
        if tmp in visited:
            return True
        visited[tmp] = 1
        tmp = tmp.next        

    return False

def tortoise_hare(head:ListNode):

    fast = head
    slow = head

    # if length of the list is odd fast.next will be null
    # if list length is even, fast will become null

    while fast and fast.next:
        # move slow one step
        slow = slow.next
        # move fast two step
        fast = fast.next.next

        if slow == fast:
            # we've found a loop
            return True
    return False


arr = [3,2,0,0]

pos = -1
cyclic_head = createLoopList(arr,pos)
normal_head = createLoopList(arr,-1)

print(has_loop(cyclic_head))
print(has_loop(normal_head))