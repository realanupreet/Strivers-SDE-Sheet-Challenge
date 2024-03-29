def cloneLL(head: Node) -> Node:
    if head is None: return None
    mapping = {}
    cur = head
    while cur:
        mapping[cur] = Node(cur.data,None,None)
        cur = cur.next
    cur = head
    while cur:
        if cur.next:
            mapping[cur].next = mapping[cur.next]
        if cur.random:
            mapping[cur].random = mapping[cur.random]
        cur = cur.next
    return mapping[head]