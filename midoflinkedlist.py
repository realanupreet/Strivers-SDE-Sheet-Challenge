# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        myhead=head
        i=0
        while myhead:
            i+=1
            myhead=myhead.next
        # print("i",i)
        a=0
        if i%2==0:
            # print(i,i.%2).
            a=(i+2)//2
        else:
            # print(i,i%2,i+1,(i+1)/2)
            a=(i+1)//2
        # print("a",a)
        nhead=head
        k=0
        while nhead:
            k+=1
            # print("k",k)
            if k==a:
                return nhead
            nhead=nhead.next
