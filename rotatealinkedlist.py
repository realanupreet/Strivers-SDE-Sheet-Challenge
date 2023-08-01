def rotate(head, k):
    if head is None or head.next is None:
        return head
    
    curr=head
    N=1
    while curr.next:
        N+=1
        curr=curr.next
    curr.next=head
    M=N-k%N
    i=0
    curr=head

    while i<M:
        prev=curr
        curr=curr.next
        i+=1
    prev.next=None
    head=curr
    return head