def reverseLL(head):
    curr = head
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


def helper(head, target):
    head = reverseLL(head)
    if target == 1:
        head = head.next
    else:
        curr = head
        while curr:
            prev = curr
            target -= 1
            curr = curr.next
            if target == 1:
                prev.next = curr.next
                break
    head = reverseLL(head)
    return head
    

def removeKthNode(head, k):
    if head is None or head.next is None:
        return None
    head = helper(head, k)
    return head