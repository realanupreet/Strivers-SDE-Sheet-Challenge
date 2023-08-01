def getListAfterReverseOperation(head, n, b):
    curr=head
    grandtail=curr
    tail=None
    for i in range(len(b)):
        if b[i]==0:
            continue
        prev=None
        j=0
        if i>0:
            tail=curr
        while curr!=None and j<b[i]:
            front=curr.next
            curr.next=prev
            prev=curr
            curr=front
            j+=1
        if i>0 and grandtail!=None:
            grandtail.next=prev
            grandtail=tail
        if i==0:
            head=prev
    if tail!=None:
        tail.next=curr
    return head

