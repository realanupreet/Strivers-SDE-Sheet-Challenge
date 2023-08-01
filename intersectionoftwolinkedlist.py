def findLength(head):
    length = 0
    while head:
        length += 1
        head = head.next
    return length


def findIntersection(firstHead, secondHead):
    firstHeadLength = findLength(firstHead)
    secondHeadLength = findLength(secondHead)
    while firstHeadLength > secondHeadLength:
        firstHead = firstHead.next
        firstHeadLength -= 1
    while secondHeadLength > firstHeadLength:
        secondHead = secondHead.next
        secondHeadLength -= 1
    while firstHead != secondHead:
        firstHead = firstHead.next
        secondHead = secondHead.next
    return firstHead