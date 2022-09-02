# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        h = head
        target_pos = 0
        while h:
            h = h.next
            target_pos += 1
        target_pos -= n
        if target_pos == 0:
            return head.next
        cnt, before, result = 0, head, head
        while head:
            if cnt != target_pos:
                cnt += 1
                before = head
                head = head.next
            else:
                before.next = head.next
                break
        return result

if __name__ == '__main__':
    # h = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    h = ListNode(1)
    print(Solution().removeNthFromEnd(h, 1))






