# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        arr = []
        while head:
            # print(head.val)
            # print("loop",arr)
            arr.append(head.val)
            head = head.next
        arr = arr[::-1]
        # print(arr)
        # print("arr[0]",arr[0] )
        ab = arr[0]
        head = ListNode(ab)
        nhead = head
        # print("head",head)
        for a in arr[1:]:
            # print("a",a)
            head.next = ListNode(a)
            head = head.next

        return nhead
