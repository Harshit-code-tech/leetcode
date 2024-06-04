# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ll, ans = [], []
        while head:
            ll.append(head.val)
            head = head.next
        
        mid = len(ll) // 2
        while mid > 0:
            ans.append(ll[mid - 1] + ll[-mid])
            mid -= 1
        
        return max(ans)